%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An HTML/XHTML template library for Ruby
Name:		amrita
Version:	1.0.2
Release:	1
License:	GPL
URL:		http://www.brain-tokyo.jp/research/amrita/
Group:		Development/Libraries
Source0:	http://www.brain-tokyo.jp/research/amrita/%{name}-%{version}.tar.gz
# Source0-md5:	903af244f72d1a4b83f2cb8cfeecbac7
BuildArchitectures:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} SITE_DIR=$RPM_BUILD_ROOT%{ruby_rubylibdir}


%files
%defattr(644,root,root,755)

%{ruby_rubylibdir}/amrita/compiler.rb
%{ruby_rubylibdir}/amrita/format.rb
%{ruby_rubylibdir}/amrita/tag.rb
%{ruby_rubylibdir}/amrita/parser.rb
%{ruby_rubylibdir}/amrita/node_expand.rb
%{ruby_rubylibdir}/amrita/node.rb
%{ruby_rubylibdir}/amrita/template.rb
%{ruby_rubylibdir}/amrita/ams.rb
%{ruby_rubylibdir}/amrita/xml.rb
%{ruby_rubylibdir}/amrita/amx.rb
%{ruby_rubylibdir}/amrita/handlers.rb
%{ruby_rubylibdir}/amrita/cgikit.rb
%{ruby_rubylibdir}/amrita/merge.rb
%{ruby_rubylibdir}/amrita/parts.rb
%attr(755,root,root) %{_bindir}/ams
%attr(755,root,root) %{_bindir}/amx
%attr(755,root,root) %{_bindir}/amshandler

%clean
rm -rf $RPM_BUILD_ROOT
