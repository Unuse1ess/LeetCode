CodeRunner.jar: clean
	mkdir /dev/shm/target
	javac -d /dev/shm/target CodeRunner.java
	jar cvmf manifest CodeRunner.jar -C /dev/shm/target/ .

clean:
	rm -rf /dev/shm/target CodeRunner.jar
	