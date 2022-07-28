
using System;
using System.Threading;
using System.Diagnostics;

class Program {
	static void Main() {

        Process curr = Process.GetCurrentProcess();
 
        // Cria a thread Filha - ThreadStart: Método a ser executado pela thread como parâmetro;
		Thread t1 = new Thread(new ThreadStart(ExecAction));
		t1.Start();

		Console.WriteLine($"Sou pai ({curr.Id})");
		
		Console.ReadKey();
	}
	static void ExecAction() {

        Process curr = Process.GetCurrentProcess();
		Console.WriteLine($"Sou filha de: {curr.Id}");

	}
}


