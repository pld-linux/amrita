%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	An HTML/XHTML template library for Ruby
Summary(pl):	Biblioteka szablonów HTML/XHTML dla jêzyka Ruby
Name:		amrita
Version:	1.0.2
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://osdn.dl.sourceforge.jp/amrita/10939/%{name}-%{version}.tar.gz
# Source0-md5:	903af244f72d1a4b83f2cb8cfeecbac7
Source1:	setup.rb
URL:		http://www.brain-tokyo.jp/research/amrita/
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML/XHTML template library for Ruby.

%description -l pl
Biblioteka szablonów HTML/XHTML dla jêzyka Ruby.

%prep
%setup -q
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

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
