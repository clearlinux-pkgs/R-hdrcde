#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-hdrcde
Version  : 3.3
Release  : 15
URL      : https://cran.r-project.org/src/contrib/hdrcde_3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/hdrcde_3.3.tar.gz
Summary  : Highest Density Regions and Conditional Density Estimation
Group    : Development/Tools
License  : GPL-3.0
Requires: R-hdrcde-lib = %{version}-%{release}
Requires: R-RColorBrewer
Requires: R-ash
Requires: R-ggplot2
Requires: R-ks
Requires: R-locfit
BuildRequires : R-RColorBrewer
BuildRequires : R-ash
BuildRequires : R-ggplot2
BuildRequires : R-ks
BuildRequires : R-locfit
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# hdrcde: Highest Density Regions and Conditional Density Estimation
[![Travis-CI Build Status](https://travis-ci.org/robjhyndman/hdrcde.svg?branch=master)](https://travis-ci.org/robjhyndman/hdrcde)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/hdrcde)](https://cran.r-project.org/package=hdrcde)
[![Downloads](http://cranlogs.r-pkg.org/badges/hdrcde)](https://cran.r-project.org/package=hdrcde)
[![Licence](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

%package lib
Summary: lib components for the R-hdrcde package.
Group: Libraries

%description lib
lib components for the R-hdrcde package.


%prep
%setup -q -c -n hdrcde

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571841824

%install
export SOURCE_DATE_EPOCH=1571841824
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hdrcde
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hdrcde
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library hdrcde
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc hdrcde || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/hdrcde/CITATION
/usr/lib64/R/library/hdrcde/DESCRIPTION
/usr/lib64/R/library/hdrcde/INDEX
/usr/lib64/R/library/hdrcde/Meta/Rd.rds
/usr/lib64/R/library/hdrcde/Meta/data.rds
/usr/lib64/R/library/hdrcde/Meta/features.rds
/usr/lib64/R/library/hdrcde/Meta/hsearch.rds
/usr/lib64/R/library/hdrcde/Meta/links.rds
/usr/lib64/R/library/hdrcde/Meta/nsInfo.rds
/usr/lib64/R/library/hdrcde/Meta/package.rds
/usr/lib64/R/library/hdrcde/NAMESPACE
/usr/lib64/R/library/hdrcde/NEWS.md
/usr/lib64/R/library/hdrcde/R/hdrcde
/usr/lib64/R/library/hdrcde/R/hdrcde.rdb
/usr/lib64/R/library/hdrcde/R/hdrcde.rdx
/usr/lib64/R/library/hdrcde/data/Rdata.rdb
/usr/lib64/R/library/hdrcde/data/Rdata.rds
/usr/lib64/R/library/hdrcde/data/Rdata.rdx
/usr/lib64/R/library/hdrcde/help/AnIndex
/usr/lib64/R/library/hdrcde/help/aliases.rds
/usr/lib64/R/library/hdrcde/help/hdrcde.rdb
/usr/lib64/R/library/hdrcde/help/hdrcde.rdx
/usr/lib64/R/library/hdrcde/help/paths.rds
/usr/lib64/R/library/hdrcde/html/00Index.html
/usr/lib64/R/library/hdrcde/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/hdrcde/libs/hdrcde.so
