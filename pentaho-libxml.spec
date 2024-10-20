%{?_javapackages_macros:%_javapackages_macros}
%if 0%{?fedora}
%else
Epoch: 1
%endif
%define origname libxml

Name: pentaho-libxml
Version: 1.1.3
Release: 11.1
Summary: Namespace aware SAX-Parser utility library
License: LGPLv2

#Original source: http://downloads.sourceforge.net/jfreereport/%%{origname}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{origname}-%{version}-jarsdeleted.zip
URL: https://reporting.pentaho.org/
BuildRequires: ant, ant-contrib, java-devel, javapackages-tools, libbase, libloader
Requires: java, javapackages-tools, libbase >= 1.1.2, libloader >= 1.1.2
BuildArch: noarch
Patch0: libxml-1.1.2-build.patch

%description
Pentaho LibXML is a namespace aware SAX-Parser utility library. It eases the
pain of implementing non-trivial SAX input handlers.

%package javadoc
Summary: Javadoc for %{name}

%if 0%{?fedora}
Requires: %{name} = %{version}-%{release}
%else
Requires: %{name} = %{EVRD}
%endif
Requires: javapackages-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
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
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{origname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{origname}-%{version}.jar %{origname}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{origname}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{origname}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{origname}-%{version}.jar
%{_javadir}/%{origname}.jar

%files javadoc
%{_javadocdir}/%{origname}

%changelog
* Tue Aug 06 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1.3-10
- ant-nodeps is dropped from ant-1.9.0-2 build in rawhide
- Drop buildroot, %%clean, %%defattr and removal of buildroot in %%install

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-7
- clarify license

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-6
- repack source to remove bundled multi-license .jars

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> - 1.1.3-3
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

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
