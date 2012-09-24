%define upstream_name libxml

Name:           pentaho-libxml
Version:        1.1.6
Release:        %mkrel 1
Summary:        Namespace aware SAX-Parser utility library
License:        LGPLv2+
Group:          System/Libraries 
Source:         http://downloads.sourceforge.net/jfreereport/%{upstream_name}-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel >= 0:1.6.0 , jpackage-utils, libbase, libloader, java-rpmbuild
Requires:       java >= 0:1.6.0 , jpackage-utils, libbase >= 1.1.2, libloader >= 1.1.2
BuildArch:      noarch
Patch0:         pentaho-libxml-1.1.2-fix-build.patch

%description
Pentaho LibXML is a namespace aware SAX-Parser utility library. It eases the
pain of implementing non-trivial SAX input handlers.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Books/Computer books 
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase libloader
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{upstream_name}-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{upstream_name}-%{version}.jar %{upstream_name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{upstream_name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{upstream_name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{upstream_name}-%{version}.jar
%{_javadir}/%{upstream_name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{upstream_name}


%changelog

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198977
- new version 1.1.6
- drop gcj support
- rediff and rename patch to fix-build.patch
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-3.mga1
+ Revision: 74300
- Really build without gcj

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-2.mga1
+ Revision: 74281
- Build without gcj

* Wed Jan 26 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 40146
- Adapt for mageia
- imported package pentaho-libxml


* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> 1.1.3
- latest version

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> 1.1.2
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-2.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-1.OOo31
- Post release tuned for OpenOffice.org reportdesigner

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-0.1.rc
- latest version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 0.9.11-1
- initial fedora import
