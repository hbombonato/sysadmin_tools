%define path /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

%define _topdir  /home/hbombonato/Projetos/sources/
%define _sourcedir 	%{_topdir}/SOURCES

Name:		jetty-init
Version:	1.0.1
Release:	1

Source0:	https://hbombonato@github.com/hbombonato/sysadmin_tools.git/SPEC/jetty/SPECS/%{name}/%{name}-%{version}/jetty

Group:		Application/Internet
Packager:	Comunit OpenSource
License:	GPL
Vendor:		Hernani Bombonato
URL:		http://github.com
Summary:	Script for the help sysadmin jetty manut

BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

Requires: jre

%description
Script for the help sysadmin jetty manut

#%prep
#%setup -n %{name}-%{version}

#%build

%install
mkdir -p "${RPM_BUILD_ROOT}/etc/init.d" "${RPM_BUILD_ROOT}/opt/"
cp "%{SOURCE0}" "${RPM_BUILD_ROOT}/etc/init.d"
find -type f -exec chmod 0644 '{}' ';'
chmod 0755 "${RPM_BUILD_ROOT}/etc/init.d/jetty"

%post
export PATH="%{path}:${PATH}"

chkconfig --add jetty	

%preun
export PATH="%{path}:${PATH}"

chkconfig --del jetty

%clean
[[ "${RPM_BUILD_ROOT}" != "/" ]] && rm -rf "${RPM_BUILD_ROOT}"

%files
/etc/init.d/jetty
/opt/webapps

%changelog
* Jul Dom  02 2011 - Hernani A Bombonato <herlix@gmail.com> release 1
	- Reescaping all variables
	- Improvement of stop/start functions and messages
	- Detecting if $SHELL exists
	- Included '-s' parameter in 'su' commands to avoid absent terminal
