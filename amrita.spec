%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An HTML/XHTML template library for Ruby
Summary(pl):	Biblioteka szablonów HTML/XHTML dla jêzyka Ruby
Name:		amrita
Version:	1.8.2
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://www.brain-tokyo.jp/research/amrita/%{name}-%{version}.tar.gz
# Source0-md5:	36dd153cef9481d853d09094b8daece7
Patch0:		%{name}-REXML.patch
URL:		http://www.brain-tokyo.jp/research/amrita/
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby.

%description -l pl
Biblioteka szablonów HTML/XHTML dla jêzyka Ruby.

%prep
%setup -q
%patch0 -p1

%build
ruby install.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby install.rb setup 
rdoc docs README -o rdoc

%install
rm -rf $RPM_BUILD_ROOT

ruby install.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog docs README RELEASENOTE sample rdoc
%lang(ja) %doc README_ja
%attr(755,root,root) %{_bindir}/ams
%attr(755,root,root) %{_bindir}/amx
%attr(755,root,root) %{_bindir}/amshandler
%dir %{ruby_rubylibdir}/amrita
%{ruby_rubylibdir}/amrita/*.rb
%attr(755,root,root) %{ruby_archdir}/amrita_accel.so
