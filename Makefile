server:
	hugo server -D --disableFastRender --ignoreCache

chroma:
	hugo gen chromastyles --style=monokai > ./assets/css/extended/chroma_dark.css
	hugo gen chromastyles --style=monokailight > ./assets/css/extended/chroma_light.css
	sed -i 's/.chroma/.dark .chroma/g' ./assets/css/extended/chroma_dark.css

update:
	git submodule update --remote --merge
