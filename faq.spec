Summary:	Frequently Asked Questions (FAQ) about Linux.
Name:		faq
Version:	6.0
Release:	2
Source:		ftp://sunsite.unc.edu/pub/Linux/docs/faqs-%{version}.tar.gz
Copyright:	distributable
Group:		Documentation
Buildroot:	/tmp/%{name}-%{version}-root
BuildArchitectures: noarch

%description
The faq package includes the text of the Frequently Asked Questions
(FAQ) about Linux from the SunSITE website
(http://sunsite.unc.edu/pub/Linux/docs/faqs/linux-faq/Linux-FAQ).
The Linux FAQ is a great source of information about Linux.

Install faq if you'd like to read the Linux FAQ off your own machine.

%prep
%setup -q -n faqs

%build
# kill a dangling symlink
rm -f Wine-FAQ
mv Threads-FAQ/Threads-FAQ-html.tar.gz Threads-FAQ/Threads-FAQ.html.tar.gz

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
