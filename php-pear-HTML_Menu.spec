%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Menu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generates HTML Menu from multidimensional hashes
Summary(pl):	%{_pearname} - generowanie menu w HTML z wielowymiarowych hashy
Name:		php-pear-%{_pearname}
Version:	2.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8d31904acff0da327e061c8f254c2645
URL:		http://pear.php.net/package/HTML_Menu/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With the %{_pearname} class one can easily create and maintain a
navigation structure for website, configuring it via a multidimensional
hash structure. Different modes for the HTML output are supported.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± klasy HTML_Menu mo¿liwe jest tworzenie i zarz±dzanie
struktur± nawigacyjn± strony WWW, konfigurowaln± za pomoc±
wielowymiarowej struktury hashy. Obs³ugiwane s± ró¿ne rodzaje wyj¶cia
HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php             $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
