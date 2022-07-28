
using System;
using System.Threading;
using System.Diagnostics;
using System.Net;

class Program {

    public static int procID;
	static void Main() {

        Process curr = Process.GetCurrentProcess();

        procID = curr.Id;
 
		Console.WriteLine($"Sou pai ({procID})");

        // Criando 5 threads, cada uma baixa a imagem
        
        Thread[] threadArr = new Thread[5];

        for (int i = 0; i < 5; i++){
            // Cria a thread Filha - ThreadStart: Método a ser executado pela thread como parâmetro;
            Thread th = new Thread(DownloadIMG);
            th.Name = "Th " + i;

            Console.WriteLine($"Thread {th.Name} criada com sucesso!");

            threadArr[i] = th;
        }

        foreach (Thread th in threadArr){
            th.Start();
        }

	}
	static void DownloadIMG() {
    
        String fileName, url; 

        WebClient cli = new WebClient();
        Stopwatch stopWhatch = new Stopwatch();

        fileName = Thread.CurrentThread.Name + ".jpg";
        url = "https://www.nasa.gov/sites/default/files/thumbnails/image/main_image_star-forming_region_carina_nircam_final-5mb.jpg";

        try {
            stopWhatch.Start();
            cli.DownloadFile(url, fileName);
            stopWhatch.Stop();
        } finally {
            Console.WriteLine($"Arquivo baixado com sucesso pela thread: {Thread.CurrentThread.Name} em {stopWhatch.Elapsed.TotalSeconds} segundos!");
            stopWhatch.Reset();
        }
	}
}
