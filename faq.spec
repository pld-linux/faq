Summary:	Frequently Asked Questions (FAQ) about Linux
Summary(pl):	FAQ - czêsto zadawane pytania na temat Linuksa
Name:		faq
Version:	6.0
Release:	2
Source0:	ftp://sunsite.unc.edu/pub/Linux/docs/%{name}s-%{version}.tar.gz
License:	distributable
Group:		Documentation
Group(de):	Dokumentation
Group(es):	Documentación
Group(pl):	Dokumentacja
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
The faq package includes the text of the Frequently Asked Questions
(FAQ) about Linux from the SunSITE website
(http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ). The
Linux FAQ is a great source of information about Linux.

Install faq if you'd like to read the Linux FAQ off your own machine.

%description -l pl
Pakiet faq zawiera tekst Najczê¶ciej Zadawanych Pytañ (i odpowiedzi)
dotycz±cych Linuksa, pochodz±cych z witryny SunSITE:
http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ/.
Linuksowe FAQ jest wspania³ym ¼ród³em wiedzy o Linuksie.

Nale¿y zainstalowaæ faq je¶li chce siê przeczytaæ FAQ dotycz±ce
systemu Linux.

%prep
%setup -q -n faqs

%build
# kill a dangling symlink
rm -f Wine-FAQ
mv -f Threads-FAQ/Threads-FAQ-html.tar.gz Threads-FAQ/Threads-FAQ.html.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/FAQ/{txt,html,ps}
for faq in *FAQ ; do
  if [ -d $faq ] ; then
    [ -f $faq/$faq ] && cp $faq/$faq $RPM_BUILD_ROOT%{_defaultdocdir}/FAQ/txt
    [ -f $faq/$faq.html.tar.gz ] && tar xzvf $faq/$faq.html.tar.gz -C $RPM_BUILD_ROOT%{_defaultdocdir}/FAQ/html
    [ -f $faq/$faq.ps.gz ] && rm -f $faq/$faq.ps.gz
  else
    cp $faq $RPM_BUILD_ROOT%{_defaultdocdir}/FAQ
  fi
done

gzip -9nf $RPM_BUILD_ROOT%{_defaultdocdir}/FAQ/*FAQ \
	$RPM_BUILD_ROOT%{_defaultdocdir}/FAQ/txt/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%docdir %{_defaultdocdir}/FAQ
%dir %{_defaultdocdir}/FAQ
%{_defaultdocdir}/FAQ/*
