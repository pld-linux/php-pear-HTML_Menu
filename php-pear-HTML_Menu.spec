# ToDo:
# - fix pl summary/description [?]
%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       Menu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generates HTML Menu from multidimensional hashes
Summary(pl):	%{_pearname} - generuje menu HTML z wielowymiarowych hashy
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	70238ce27fb0edcf744277f660a5d3a1
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the %{_pearname} class one can easily create and maintain a
navigation structure for website, configuring it via a multidimensional
hash structure. Different modes for the HTML output are supported.

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc± %{_pearname} mo¿liwe jest tworzenie i zarz±dzanie struktur±
nawigacyjn± strony www, konfigurowywaln± za pomoc± wielowymiarowej
struktury hashowalnej. Wspierane s± ró¿ne sposoby wyj¶cia HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
