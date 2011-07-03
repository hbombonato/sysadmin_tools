%define path /usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

%define _topdir  /home/hbombonato/rpmbuild
%define _sourcedir 	%{_topdir}/SOURCES


Name:	 jetty
Version: 6.1.25
Release: 1

Source:	 jetty-6.1.25.tar.gz

Group:	 Application/Internet
Packager: IG - Internet Group
License: GPL
Vendor:	 Internet Group
URL:	 http://jetty.codehaus.org/jetty/
Summary: The Jetty Webserver and Servlet Container

BuildRoot: %{_tmppath}/jetty-6.1.25
BuildArch: noarch

Requires: jre
Requires: jetty-init


%description
Jetty is a 100% Java HTTP Server and Servlet Container

%prep
%setup -c jetty-6.1.25

#%build

%install
mkdir -p "${RPM_BUILD_ROOT}/usr/local"
cp -a "%{_topdir}/BUILD/jetty-6.1.25" "${RPM_BUILD_ROOT}/usr/local/"
find -type d -exec chmod 0755 '{}' ';'
find -type f -exec chmod 0644 '{}' ';'

%post

%preun

%clean
[[ "${RPM_BUILD_ROOT}" != "/" ]] && rm -rf "${RPM_BUILD_ROOT}"

%files
/usr/local/jetty-6.1.25

%changelog
* Jul iDom 02 2011 - Hernani A Bombonato <herlix@gmail.com> release 1
 - Initial version
		- Information this is READEME
