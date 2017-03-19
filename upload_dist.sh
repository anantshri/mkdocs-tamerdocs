#!/bin/bash
NAME=`grep "name" setup.py | cut -d"\"" -f2`
WNAME=`echo $NAME |tr "-" "_"`
VERSION=`grep "VERSION=" setup.py | cut -f2 -d"'"`
TEST=false
TESTPY=""
if [ "$TEST" = true ]; then
	TESTPY="-r testpypi"
fi
echo "Building $NAME version $VERSION"
python setup.py sdist bdist_wheel
cd dist
gpg --detach-sign -a "$NAME-"$VERSION".tar.gz"
cd ..
echo "Registering product"
twine register dist/$WNAME-$VERSION-py2-none-any.whl $TESTPY
twine register dist/$NAME-$VERSION.tar.gz $TESTPY
echo "uploading product"
twine upload dist/* $TESTPY
