Summary:	Frequently Asked Questions (FAQ) about Linux
Summary(pl.UTF-8):	FAQ - często zadawane pytania na temat Linuksa
Name:		faq
Version:	6.0
Release:	2
Source0:	ftp://sunsite.unc.edu/pub/Linux/docs/%{name}s-%{version}.tar.gz
# Source0-md5:	9d036492928ab1d65192738beff5812c
License:	distributable
Group:		Documentation
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The faq package includes the text of the Frequently Asked Questions
(FAQ) about Linux from the SunSITE website
(http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ). The
Linux FAQ is a great source of information about Linux.

Install faq if you'd like to read the Linux FAQ off your own machine.

%description -l pl.UTF-8
Pakiet faq zawiera tekst Najczęściej Zadawanych Pytań (i odpowiedzi)
dotyczących Linuksa, pochodzących z witryny SunSITE:
http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ/.
Linuksowe FAQ jest wspaniałym źródłem wiedzy o Linuksie.

Należy zainstalować faq jeśli chce się przeczytać FAQ dotyczące
systemu Linux.

%prep
%setup -q -n %{name}s

%build
# kill a dangling symlink
rm -f Wine-FAQ
mv -f Threads-FAQ/Threads-FAQ-html.tar.gz Threads-FAQ/Threads-FAQ.html.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/FAQ/{txt,html,ps}
for faq in *FAQ; do
	if [ -d $faq ]; then
		if [ -f $faq/$faq ]; then cp $faq/$faq $RPM_BUILD_ROOT%{_docdir}/FAQ/txt; fi
		if [ -f $faq/$faq.html.tar.gz ]; then tar xzvf $faq/$faq.html.tar.gz -C $RPM_BUILD_ROOT%{_docdir}/FAQ/html; fi
		if [ -f $faq/$faq.ps.gz ]; then rm -f $faq/$faq.ps.gz; fi
	else
		cp $faq $RPM_BUILD_ROOT%{_docdir}/FAQ
	fi
done

gzip -9nf $RPM_BUILD_ROOT%{_docdir}/FAQ/*FAQ \
	$RPM_BUILD_ROOT%{_docdir}/FAQ/txt/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_docdir}/FAQ
%dir %{_docdir}/FAQ
%{_docdir}/FAQ/*
