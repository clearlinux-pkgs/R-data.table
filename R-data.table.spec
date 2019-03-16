#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-data.table
Version  : 1.12.0
Release  : 22
URL      : https://cran.r-project.org/src/contrib/data.table_1.12.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/data.table_1.12.0.tar.gz
Summary  : Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins, fast add/modify/delete of columns by group using no copies at all, list columns and a fast file reader (fread). Offers a natural and flexible syntax, for faster development.
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: R-data.table-lib = %{version}-%{release}
Requires: R-bit64
BuildRequires : R-bit64
BuildRequires : buildreq-R

%description
### Overview is on the project's [homepage](http://r-datatable.com).

%package lib
Summary: lib components for the R-data.table package.
Group: Libraries

%description lib
lib components for the R-data.table package.


%prep
%setup -q -c -n data.table

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547396065

%install
export SOURCE_DATE_EPOCH=1547396065
rm -rf %{buildroot}
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library data.table
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library data.table
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library data.table
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library data.table|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/data.table/DESCRIPTION
/usr/lib64/R/library/data.table/INDEX
/usr/lib64/R/library/data.table/LICENSE
/usr/lib64/R/library/data.table/Meta/Rd.rds
/usr/lib64/R/library/data.table/Meta/features.rds
/usr/lib64/R/library/data.table/Meta/hsearch.rds
/usr/lib64/R/library/data.table/Meta/links.rds
/usr/lib64/R/library/data.table/Meta/nsInfo.rds
/usr/lib64/R/library/data.table/Meta/package.rds
/usr/lib64/R/library/data.table/Meta/vignette.rds
/usr/lib64/R/library/data.table/NAMESPACE
/usr/lib64/R/library/data.table/NEWS.md
/usr/lib64/R/library/data.table/R/data.table
/usr/lib64/R/library/data.table/R/data.table.rdb
/usr/lib64/R/library/data.table/R/data.table.rdx
/usr/lib64/R/library/data.table/doc/datatable-benchmarking.Rmd
/usr/lib64/R/library/data.table/doc/datatable-benchmarking.html
/usr/lib64/R/library/data.table/doc/datatable-faq.R
/usr/lib64/R/library/data.table/doc/datatable-faq.Rmd
/usr/lib64/R/library/data.table/doc/datatable-faq.html
/usr/lib64/R/library/data.table/doc/datatable-importing.Rmd
/usr/lib64/R/library/data.table/doc/datatable-importing.html
/usr/lib64/R/library/data.table/doc/datatable-intro.R
/usr/lib64/R/library/data.table/doc/datatable-intro.Rmd
/usr/lib64/R/library/data.table/doc/datatable-intro.html
/usr/lib64/R/library/data.table/doc/datatable-keys-fast-subset.R
/usr/lib64/R/library/data.table/doc/datatable-keys-fast-subset.Rmd
/usr/lib64/R/library/data.table/doc/datatable-keys-fast-subset.html
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.R
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.Rmd
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.html
/usr/lib64/R/library/data.table/doc/datatable-reshape.R
/usr/lib64/R/library/data.table/doc/datatable-reshape.Rmd
/usr/lib64/R/library/data.table/doc/datatable-reshape.html
/usr/lib64/R/library/data.table/doc/datatable-secondary-indices-and-auto-indexing.R
/usr/lib64/R/library/data.table/doc/datatable-secondary-indices-and-auto-indexing.Rmd
/usr/lib64/R/library/data.table/doc/datatable-secondary-indices-and-auto-indexing.html
/usr/lib64/R/library/data.table/doc/index.html
/usr/lib64/R/library/data.table/help/AnIndex
/usr/lib64/R/library/data.table/help/aliases.rds
/usr/lib64/R/library/data.table/help/data.table.rdb
/usr/lib64/R/library/data.table/help/data.table.rdx
/usr/lib64/R/library/data.table/help/paths.rds
/usr/lib64/R/library/data.table/html/00Index.html
/usr/lib64/R/library/data.table/html/R.css
/usr/lib64/R/library/data.table/libs/symbols.rds
/usr/lib64/R/library/data.table/tests/1206FUT.txt
/usr/lib64/R/library/data.table/tests/1680-fread-header-encoding.csv
/usr/lib64/R/library/data.table/tests/2008head.csv
/usr/lib64/R/library/data.table/tests/530_fread.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_1.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_2.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_3_extreme.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_4.txt
/usr/lib64/R/library/data.table/tests/SA2-by-DJZ.csv
/usr/lib64/R/library/data.table/tests/allchar.csv.gz
/usr/lib64/R/library/data.table/tests/alluniquechar.csv
/usr/lib64/R/library/data.table/tests/bad.txt
/usr/lib64/R/library/data.table/tests/benchmark.Rraw
/usr/lib64/R/library/data.table/tests/ch11b.dat
/usr/lib64/R/library/data.table/tests/colnames4096.csv
/usr/lib64/R/library/data.table/tests/doublequote_newline.csv
/usr/lib64/R/library/data.table/tests/fillheader.csv
/usr/lib64/R/library/data.table/tests/fread_blank.txt
/usr/lib64/R/library/data.table/tests/fread_blank2.txt
/usr/lib64/R/library/data.table/tests/fread_blank3.txt
/usr/lib64/R/library/data.table/tests/fread_line_error.csv
/usr/lib64/R/library/data.table/tests/gb18030.txt
/usr/lib64/R/library/data.table/tests/genotypes_genome.txt
/usr/lib64/R/library/data.table/tests/grr.csv.gz
/usr/lib64/R/library/data.table/tests/isoweek_test.csv
/usr/lib64/R/library/data.table/tests/issue_1087_utf8_bom.csv
/usr/lib64/R/library/data.table/tests/issue_1095_fread.txt
/usr/lib64/R/library/data.table/tests/issue_1113_fread.txt
/usr/lib64/R/library/data.table/tests/issue_1116_fread_few_lines.txt
/usr/lib64/R/library/data.table/tests/issue_1116_fread_few_lines_2.txt
/usr/lib64/R/library/data.table/tests/issue_1164_json.txt
/usr/lib64/R/library/data.table/tests/issue_1330_fread.txt
/usr/lib64/R/library/data.table/tests/issue_1462_fread_quotes.txt
/usr/lib64/R/library/data.table/tests/issue_1573_fill.txt
/usr/lib64/R/library/data.table/tests/issue_2051.csv
/usr/lib64/R/library/data.table/tests/issue_2157_sampling_overlap.txt.gz
/usr/lib64/R/library/data.table/tests/issue_2157_sampling_reached_eof_early.txt.bz2
/usr/lib64/R/library/data.table/tests/issue_563_fread.txt
/usr/lib64/R/library/data.table/tests/issue_773_fread.txt
/usr/lib64/R/library/data.table/tests/issue_785_fread.txt
/usr/lib64/R/library/data.table/tests/iterations.txt
/usr/lib64/R/library/data.table/tests/melt-warning-1752.tsv
/usr/lib64/R/library/data.table/tests/onecol4096.csv
/usr/lib64/R/library/data.table/tests/other.Rraw
/usr/lib64/R/library/data.table/tests/quoted_multiline.csv
/usr/lib64/R/library/data.table/tests/quoted_no_header.csv
/usr/lib64/R/library/data.table/tests/russellCRCRLF.csv
/usr/lib64/R/library/data.table/tests/russellCRLF.csv
/usr/lib64/R/library/data.table/tests/session_aborted_fatal_error.txt
/usr/lib64/R/library/data.table/tests/test0.txt
/usr/lib64/R/library/data.table/tests/test1372.Rdata
/usr/lib64/R/library/data.table/tests/tests-DESCRIPTION
/usr/lib64/R/library/data.table/tests/tests.Rraw
/usr/lib64/R/library/data.table/tests/unescaped.csv
/usr/lib64/R/library/data.table/tests/utf16be.txt
/usr/lib64/R/library/data.table/tests/utf16le.txt
/usr/lib64/R/library/data.table/tests/winallquoted.csv.bz2

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/data.table/libs/datatable.so
/usr/lib64/R/library/data.table/libs/datatable.so.avx2
/usr/lib64/R/library/data.table/libs/datatable.so.avx512
