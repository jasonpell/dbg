all: lib_files python_files

clean:
	cd lib && make clean
	cd python && make clean

lib_files:
	cd lib && make

python_files:
	cd python && make
