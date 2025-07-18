Summary:	An HTML/XHTML template library for Ruby
Summary(pl.UTF-8):	Biblioteka szablonów HTML/XHTML dla języka Ruby
Name:		amrita
Version:	1.0.2
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://osdn.dl.sourceforge.jp/amrita/10939/%{name}-%{version}.tar.gz
# Source0-md5:	903af244f72d1a4b83f2cb8cfeecbac7
Source1:	setup.rb
Patch0:		%{name}-rexml.patch
Patch1:		%{name}-xml-fubar.patch
URL:		http://www.brain-tokyo.jp/research/amrita/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby.

%description -l pl.UTF-8
Biblioteka szablonów HTML/XHTML dla języka Ruby.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README docs/QuickStart  docs/Tour docs/Tour2 docs/XML docs/Cgi lib/amrita README_ja docs/QuickStart_ja docs/Tour_ja docs/XML_ja docs/Tour2_ja docs/Cgi_ja
cd rdoc/files/
ruby -i.back -ne 'print gsub("iso-8859-1", "EUC-JP") unless /<?xml/' *ja.html
cd ../../
cd rdoc/files/docs/
ruby -i.back -ne 'print gsub("iso-8859-1", "EUC-JP") unless /<?xml/' *ja.html
cd ../../

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog sample rdoc/*
%attr(755,root,root) %{_bindir}/ams
%attr(755,root,root) %{_bindir}/amx
%attr(755,root,root) %{_bindir}/amshandler
%dir %{ruby_rubylibdir}/amrita
%{ruby_rubylibdir}/amrita/*.rb
