build:
	bash build.sh	

run: build
	nohup ./build/Rasterizer > run.log 2>&1 &

img: build
	./build/Rasterizer -r 20 a.png

clean:
	rm -rf build

gdb: build
	gdb --args ./build/Rasterizer -r 20 a.png
