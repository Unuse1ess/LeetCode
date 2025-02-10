CodeRunner.jar: clean
	mkdir target
	javac -d target CodeRunner.java
	jar cvmf manifest CodeRunner.jar -C target/ .

clean:
	rm -rf target CodeRunner.jar
	