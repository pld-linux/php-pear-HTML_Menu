%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Menu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - generates HTML Menu from multidimensional hashes
Summary(pl.UTF-8):	%{_pearname} - generowanie menu w HTML z wielowymiarowych hashy
Name:		php-pear-%{_pearname}
Version:	2.1.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4de54dac7570a3e2bc42057b67619b4b
URL:		http://pear.php.net/package/HTML_Menu/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTML/Template/Sigma.*)'

%description
With the %{_pearname} class one can easily create and maintain a
navigation structure for website, configuring it via a multidimensional
hash structure. Different modes for the HTML output are supported.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą klasy HTML_Menu możliwe jest tworzenie i zarządzanie
strukturą nawigacyjną strony WWW, konfigurowalną za pomocą
wielowymiarowej struktury hashy. Obsługiwane są różne rodzaje wyjścia
HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
