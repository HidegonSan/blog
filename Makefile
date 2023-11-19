.PHONY:
	server chroma papermod instantpage update debug-make-posts debug-delete-posts new-%

server:
	hugo server -D --disableFastRender --ignoreCache

chroma:
	hugo gen chromastyles --style=monokai > ./assets/css/chroma/chroma_dark.css
	hugo gen chromastyles --style=monokailight > ./assets/css/chroma/chroma_light.css
	sed -i 's/.chroma/.dark .chroma/g' ./assets/css/chroma/chroma_dark.css
	python chroma.py

papermod:
	git submodule update --remote --merge

instantpage:
	git clone git@github.com:instantpage/instant.page.git tmp/instant.page && \
	cd ./tmp/instant.page && \
	npm install uglify-js && \
	npx --yes uglifyjs ./instantpage.js --compress --mangle --toplevel --output ./instantpage.min.js && \
	sed -i '1s/^/\n\/\*\n\n/' LICENSE && \
	echo -e "\n*/" >> LICENSE && \
	cat LICENSE >> ./instantpage.min.js && \
	cp ./instantpage.min.js ./../../assets/js/instantpage.js && \
	cd ./../../ && \
	rm -rf ./tmp

update: papermod instantpage

debug-make-posts:
	for i in `seq 0 1 50`; do\
		hugo new posts/__test_$$i.md;\
	done

debug-delete-posts:
	for i in `seq 0 1 50`; do\
		rm ./content/posts/__test_$$i.md;\
	done

# Thanks: http://puni56.net/posts/makefile-arg/
new-%:
	hugo new posts/${@:new-%=%}/index.md
