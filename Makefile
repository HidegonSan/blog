server:
	hugo server -D --disableFastRender --ignoreCache

chroma:
	hugo gen chromastyles --style=monokai > ./assets/css/extended/chroma_dark.css
	hugo gen chromastyles --style=monokailight > ./assets/css/extended/chroma_light.css
	sed -i 's/.chroma/.dark .chroma/g' ./assets/css/extended/chroma_dark.css

update:
	git submodule update --remote --merge

debug-make-posts:
	for i in `seq 0 1 50`; do\
		hugo new posts/__test_$$i.md;\
	done

debug-delete-posts:
	for i in `seq 0 1 50`; do\
		rm ./content/posts/__test_$$i.md;\
	done