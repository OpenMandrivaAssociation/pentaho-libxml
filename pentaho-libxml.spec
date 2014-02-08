%define upstream_name libxml

Summary:	Namespace aware SAX-Parser utility library
Name:		pentaho-libxml
Version:	1.1.6
Release:	2
License:	LGPLv2+
Group:		System/Libraries 
Url:		http://reporting.pentaho.org/
Source0:	http://downloads.sourceforge.net/jfreereport/%{upstream_name}-%{version}.zip
Patch0:		pentaho-libxml-1.1.2-fix-build.patch
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	ant-contrib
BuildRequires:	ant-nodeps
BuildRequires:	java-devel >= 0:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	libbase
BuildRequires:	libloader
BuildRequires:	java-rpmbuild
Requires:	java >= 0:1.6.0
Requires:	jpackage-utils
Requires:	libbase >= 1.1.2
Requires:	libloader >= 1.1.2

%description
Pentaho LibXML is a namespace aware SAX-Parser utility library. It eases the
pain of implementing non-trivial SAX input handlers.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java	
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

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
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{upstream_name}-%{version}.jar
%{_javadir}/%{upstream_name}.jar

%files javadoc
%{_javadocdir}/%{upstream_name}

