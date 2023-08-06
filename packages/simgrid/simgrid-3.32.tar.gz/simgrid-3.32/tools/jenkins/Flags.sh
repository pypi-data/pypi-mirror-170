#!/usr/bin/env sh

set -e

echo "Starting Flags.sh $*"

die() {
    echo "$@"
    exit 1
}

# Get an ON/OFF string from a command:
onoff() {
  if "$@" > /dev/null ; then
    echo ON
  else
    echo OFF
  fi
}

[ $# -eq 5 ] || die "Needs 5 arguments : JAVA MC SMPI DEBUG MSG"

### Cleanup previous runs

[ -n "$WORKSPACE" ] || die "No WORKSPACE"
[ -d "$WORKSPACE" ] || die "WORKSPACE ($WORKSPACE) does not exist"

do_cleanup() {
  for d
  do
    if [ -d "$d" ]
    then
      rm -rf "$d" || die "Could not remove $d"
    fi
    mkdir "$d" || die "Could not create $d"
  done
}

do_cleanup "$WORKSPACE/build"

NUMPROC="$(nproc)" || NUMPROC=1

cd "$WORKSPACE"/build

#we can't just receive ON or OFF as values as display is bad in the resulting jenkins matrix

if [ "$1" = "JAVA" ]
then
  buildjava="ON"
else
  buildjava="OFF"
fi

if [ "$2" = "MC" ]
then
  buildmc="ON"
else
  buildmc="OFF"
fi

if [ "$3" = "SMPI" ]
then
  buildsmpi="ON"
else
  buildsmpi="OFF"
fi

if [ "$4" = "DEBUG" ]
then
  builddebug="ON"
else
  builddebug="OFF"
fi

if [ "$5" = "MSG" ]
then
  buildmsg="ON"
else
  buildmsg="OFF"
fi

if [ $buildmsg = "OFF" ] && [ $buildjava = "ON" ]
then
  echo "Don't even try to build Java without MSG"
  exit 0
fi

echo "Step ${STEP}/${NSTEPS} - Building with java=${buildjava}, debug=${builddebug}, SMPI=${buildsmpi}, MC=${buildmc}, MSG=${buildmsg}"
cmake -Denable_documentation=OFF -Denable_java=${buildjava} -Denable_msg=${buildmsg} \
      -Denable_compile_optimizations=OFF -Denable_compile_warnings=ON \
      -Denable_mallocators=ON -Denable_debug=${builddebug} \
      -Denable_smpi=${buildsmpi} -Denable_smpi_MPICH3_testsuite=${buildsmpi} -Denable_model-checking=${buildmc} \
      -Denable_memcheck=OFF -Denable_memcheck_xml=OFF -Denable_smpi_MBI_testsuite=OFF \
      -Denable_ns3=$(onoff test "$buildmc" != "ON") -DNS3_HINT=/builds/ns-3-dev/build/ \
      -Denable_coverage=OFF -DLTO_EXTRA_FLAG="auto" -DCMAKE_CXX_COMPILER_LAUNCHER=ccache \
      "$WORKSPACE"

make -j$NUMPROC tests
cd ..
rm -rf build
