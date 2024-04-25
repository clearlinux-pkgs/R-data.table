#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : R-data.table
Version  : 1.15.4
Release  : 73
URL      : https://cran.r-project.org/src/contrib/data.table_1.15.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/data.table_1.15.4.tar.gz
Summary  : Extension of `data.frame`
Group    : Development/Tools
License  : MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: R-data.table-lib = %{version}-%{release}
Requires: R-data.table-license = %{version}-%{release}
BuildRequires : buildreq-R

%description
# data.table <a href="https://r-datatable.com"><img src="https://raw.githubusercontent.com/Rdatatable/data.table/master/.graphics/logo.png" align="right" height="140" /></a>

%package lib
Summary: lib components for the R-data.table package.
Group: Libraries
Requires: R-data.table-license = %{version}-%{release}

%description lib
lib components for the R-data.table package.


%package license
Summary: license components for the R-data.table package.
Group: Default

%description license
license components for the R-data.table package.


%prep
%setup -q -n data.table
pushd ..
cp -a data.table buildavx2
popd
pushd ..
cp -a data.table buildavx512
popd
pushd ..
cp -a data.table buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712004210

%install
export SOURCE_DATE_EPOCH=1712004210
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-data.table
cp %{_builddir}/data.table/LICENSE %{buildroot}/usr/share/package-licenses/R-data.table/9744cedce099f727b327cd9913a1fdc58a7f5599 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/data.table/cc
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
/usr/lib64/R/library/data.table/doc/datatable-programming.R
/usr/lib64/R/library/data.table/doc/datatable-programming.Rmd
/usr/lib64/R/library/data.table/doc/datatable-programming.html
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.R
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.Rmd
/usr/lib64/R/library/data.table/doc/datatable-reference-semantics.html
/usr/lib64/R/library/data.table/doc/datatable-reshape.R
/usr/lib64/R/library/data.table/doc/datatable-reshape.Rmd
/usr/lib64/R/library/data.table/doc/datatable-reshape.html
/usr/lib64/R/library/data.table/doc/datatable-sd-usage.R
/usr/lib64/R/library/data.table/doc/datatable-sd-usage.Rmd
/usr/lib64/R/library/data.table/doc/datatable-sd-usage.html
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
/usr/lib64/R/library/data.table/include/datatableAPI.h
/usr/lib64/R/library/data.table/po/en@quot/LC_MESSAGES/R-data.table.mo
/usr/lib64/R/library/data.table/po/en@quot/LC_MESSAGES/data.table.mo
/usr/lib64/R/library/data.table/po/zh_CN/LC_MESSAGES/R-data.table.mo
/usr/lib64/R/library/data.table/po/zh_CN/LC_MESSAGES/data.table.mo
/usr/lib64/R/library/data.table/tests/1206FUT.txt.bz2
/usr/lib64/R/library/data.table/tests/1680-fread-header-encoding.csv
/usr/lib64/R/library/data.table/tests/2008head.csv.bz2
/usr/lib64/R/library/data.table/tests/530_fread.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_1.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_2.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_3_extreme.txt
/usr/lib64/R/library/data.table/tests/536_fread_fill_4.txt
/usr/lib64/R/library/data.table/tests/SA2-by-DJZ.csv.gz
/usr/lib64/R/library/data.table/tests/allchar.csv.gz
/usr/lib64/R/library/data.table/tests/alluniquechar.csv.gz
/usr/lib64/R/library/data.table/tests/autoprint.R
/usr/lib64/R/library/data.table/tests/autoprint.Rout.save
/usr/lib64/R/library/data.table/tests/bad.txt.bz2
/usr/lib64/R/library/data.table/tests/benchmark.Rraw.bz2
/usr/lib64/R/library/data.table/tests/ch11b.dat.bz2
/usr/lib64/R/library/data.table/tests/colnames4096.csv.bz2
/usr/lib64/R/library/data.table/tests/csvy/test.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_attributes.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_comment.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_extraneous.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_incomplete_header.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_missing_type.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_override_dec.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_override_header.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_override_na.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_override_quote.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_override_sep.csvy
/usr/lib64/R/library/data.table/tests/csvy/test_skip.csvy
/usr/lib64/R/library/data.table/tests/doublequote_newline.csv
/usr/lib64/R/library/data.table/tests/fillheader.csv.bz2
/usr/lib64/R/library/data.table/tests/fread_blank.txt
/usr/lib64/R/library/data.table/tests/fread_blank2.txt
/usr/lib64/R/library/data.table/tests/fread_blank3.txt
/usr/lib64/R/library/data.table/tests/fread_line_error.csv.bz2
/usr/lib64/R/library/data.table/tests/froll.R
/usr/lib64/R/library/data.table/tests/froll.Rraw.bz2
/usr/lib64/R/library/data.table/tests/gb18030.txt
/usr/lib64/R/library/data.table/tests/genotypes_genome.txt.bz2
/usr/lib64/R/library/data.table/tests/grr.csv.gz
/usr/lib64/R/library/data.table/tests/isoweek_test.csv.bz2
/usr/lib64/R/library/data.table/tests/issue_1087_utf8_bom.csv
/usr/lib64/R/library/data.table/tests/issue_1095_fread.txt.bz2
/usr/lib64/R/library/data.table/tests/issue_1113_fread.txt.bz2
/usr/lib64/R/library/data.table/tests/issue_1116_fread_few_lines.txt.gz
/usr/lib64/R/library/data.table/tests/issue_1116_fread_few_lines_2.txt.gz
/usr/lib64/R/library/data.table/tests/issue_1164_json.txt
/usr/lib64/R/library/data.table/tests/issue_1330_fread.txt
/usr/lib64/R/library/data.table/tests/issue_1462_fread_quotes.txt.gz
/usr/lib64/R/library/data.table/tests/issue_1573_fill.txt
/usr/lib64/R/library/data.table/tests/issue_2051.csv.gz
/usr/lib64/R/library/data.table/tests/issue_2157_sampling_overlap.txt.gz
/usr/lib64/R/library/data.table/tests/issue_2157_sampling_reached_eof_early.txt.bz2
/usr/lib64/R/library/data.table/tests/issue_3400_fread.txt
/usr/lib64/R/library/data.table/tests/issue_563_fread.txt
/usr/lib64/R/library/data.table/tests/issue_773_fread.txt
/usr/lib64/R/library/data.table/tests/issue_785_fread.txt.gz
/usr/lib64/R/library/data.table/tests/iterations.txt.bz2
/usr/lib64/R/library/data.table/tests/knitr.R
/usr/lib64/R/library/data.table/tests/knitr.Rmd
/usr/lib64/R/library/data.table/tests/knitr.Rout.mock
/usr/lib64/R/library/data.table/tests/knitr.Rout.save
/usr/lib64/R/library/data.table/tests/main.R
/usr/lib64/R/library/data.table/tests/melt-warning-1752.tsv.gz
/usr/lib64/R/library/data.table/tests/melt_1754.R.gz
/usr/lib64/R/library/data.table/tests/melt_1754_synth.csv.bz2
/usr/lib64/R/library/data.table/tests/multi-file.zip
/usr/lib64/R/library/data.table/tests/nafill.R
/usr/lib64/R/library/data.table/tests/nafill.Rraw.bz2
/usr/lib64/R/library/data.table/tests/noquote.csv.gz
/usr/lib64/R/library/data.table/tests/onecol4096.csv.bz2
/usr/lib64/R/library/data.table/tests/other.R
/usr/lib64/R/library/data.table/tests/other.Rraw.bz2
/usr/lib64/R/library/data.table/tests/programming.R
/usr/lib64/R/library/data.table/tests/programming.Rraw.bz2
/usr/lib64/R/library/data.table/tests/quoted_multiline.csv.bz2
/usr/lib64/R/library/data.table/tests/quoted_no_header.csv
/usr/lib64/R/library/data.table/tests/russellCRCRLF.csv
/usr/lib64/R/library/data.table/tests/russellCRLF.csv
/usr/lib64/R/library/data.table/tests/russellCRLF.tar
/usr/lib64/R/library/data.table/tests/russellCRLF.zip
/usr/lib64/R/library/data.table/tests/session_aborted_fatal_error.txt.bz2
/usr/lib64/R/library/data.table/tests/test0.txt.bz2
/usr/lib64/R/library/data.table/tests/test1372-1.Rdata
/usr/lib64/R/library/data.table/tests/test1372.Rdata
/usr/lib64/R/library/data.table/tests/test2224.Rdata
/usr/lib64/R/library/data.table/tests/test2233-43.Rdata
/usr/lib64/R/library/data.table/tests/tests.Rraw.bz2
/usr/lib64/R/library/data.table/tests/types.R
/usr/lib64/R/library/data.table/tests/types.Rraw.bz2
/usr/lib64/R/library/data.table/tests/unescaped.csv
/usr/lib64/R/library/data.table/tests/utf16be.txt
/usr/lib64/R/library/data.table/tests/utf16le.txt
/usr/lib64/R/library/data.table/tests/winallquoted.csv.bz2

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/data.table/libs/data_table.so
/V4/usr/lib64/R/library/data.table/libs/data_table.so
/VA/usr/lib64/R/library/data.table/libs/data_table.so
/usr/lib64/R/library/data.table/libs/data_table.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-data.table/9744cedce099f727b327cd9913a1fdc58a7f5599
