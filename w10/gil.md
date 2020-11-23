**Global Interpreter Lock (GIL)** - способ синхронизации потоков. Он позволяет лишь одному потоку захватывать работу интерпретатора в единицу времени. По этой причине создание нескольких потоков не приведет к их исполнению на разных ядрах процессора. Multiprocessing свободен от этого, т.к. способствует созданию нескольких *процессов*, которые исполняются независимо друг от друга (не пересекаются пёо ссылкам на объекты). 