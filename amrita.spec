%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An HTML/XHTML template library for Ruby
Name:		amrita
Version:	1.8.2
Release:	1
License:	GPL
URL:		http://www.brain-tokyo.jp/research/amrita/
Group:		Development/Libraries
Source0:	http://www.brain-tokyo.jp/research/amrita/%{name}-%{version}.tar.gz
# Source0-md5:	36dd153cef9481d853d09094b8daece7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby

%prep
%setup -q

%build
ruby install.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby install.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby install.rb install --prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ams
%attr(755,root,root) %{_bindir}/amx
%attr(755,root,root) %{_bindir}/amshandler
%dir %{ruby_rubylibdir}/amrita
%{ruby_rubylibdir}/amrita/*.rb
%attr(755,root,root) %{ruby_archdir}/amrita_accel.so


%clean
rm -rf $RPM_BUILD_ROOT
