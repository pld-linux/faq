Summary: Frequently Asked Questions (FAQ) about Linux.
Name: faq
%define version 6.0
Version: %{version}
Release: 1
Source: ftp://sunsite.unc.edu/pub/Linux/docs/faqs-%{version}.tar.gz
Copyright: distributable
Group: Documentation
BuildArchitectures: noarch
Buildroot: /var/tmp/faq-root

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
mkdir -p $RPM_BUILD_ROOT/usr/doc/FAQ/{txt,html,ps}
for faq in *FAQ ; do
  if [ -d $faq ] ; then
    [ -f $faq/$faq ] && cp $faq/$faq $RPM_BUILD_ROOT/usr/doc/FAQ/txt
    [ -f $faq/$faq.html.tar.gz ] && tar xzvf $faq/$faq.html.tar.gz -C $RPM_BUILD_ROOT/usr/doc/FAQ/html
    [ -f $faq/$faq.ps.gz ] && rm -f $faq/$faq.ps.gz
  else
    cp $faq $RPM_BUILD_ROOT/usr/doc/FAQ/txt
  fi
done

%files
%defattr(-,root,root)
%docdir /usr/doc/FAQ
%dir /usr/doc/FAQ
%attr(-,root,root) /usr/doc/FAQ/*

%clean
rm -rf $RPM_BUILD_ROOT
