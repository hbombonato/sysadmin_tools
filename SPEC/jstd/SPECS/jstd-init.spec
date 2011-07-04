%define path /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

%define _topdir  /root/rpmbuild
%define _sourcedir 	%{_topdir}/SOURCES

Name:		jstd-init
Version:	1.0
Release:	1

Source0:	https://tools.intranet/hg/infra/tags/scripts/%{name}/%{name}-%{version}/jstd

Group:		Application/Internet
Packager:	IG - Internet Group
License:	GPL
Vendor:		Internet Group
URL:		https://tools.intranet/hg/infra/tags/scripts/%{name}/%{name}-%{version}
Summary:	Estrutura de start para aplicacoes java standalone

BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

Requires:	jre

%description
Script de apoio para aplicacoes java standalone, com base em arquivo de config.

#%prep
#%setup -n %{name}-%{version}

#%build

%install
mkdir -p "${RPM_BUILD_ROOT}/etc/init.d"
cp "%{SOURCE0}" "${RPM_BUILD_ROOT}/etc/init.d"
find -type d -exec chmod 0755 '{}' ';'
find -type f -exec chmod 0644 '{}' ';'
chmod 0755 "${RPM_BUILD_ROOT}/etc/init.d/jstd"

%post
export PATH="%{path}:${PATH}"

chkconfig --add jstd

%preun
export PATH="%{path}:${PATH}"

chkconfig --del jstd

%clean
[[ "${RPM_BUILD_ROOT}" != "/" ]] && rm -rf "${RPM_BUILD_ROOT}"

%files
/etc/init.d/jstd

%changelog
* Sun Sep 13 2010 - Hernani A Bombonato <hbombonato@ig.com> release 1
	- Reescaping all variables
	- Improvement of stop/start/restart/status/check/list/help functions and messages
	- Detecting if $SHELL exists
	- Included '-s' parameter in 'su' commands to avoid absent terminal
