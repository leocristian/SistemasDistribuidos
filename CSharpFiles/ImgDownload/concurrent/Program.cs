using System;
using System.Threading;
using System.Diagnostics;
using System.Net;

namespace download_img_concurrent;
class Program {
    public static int THREAD_NUMBER = 10;
    public static int j;
    static void Main() {
        Thread[] threadArr = new Thread[THREAD_NUMBER];

        Stopwatch watch = new Stopwatch();
        
        watch.Start();
        for (int i = 0; i < THREAD_NUMBER; i++) {
            j = i;
            Thread t = new Thread(ExecuteThread);
            t.Name = "t " + i;
            threadArr[i] = t;
            t.Start();
        }

        foreach (Thread t in threadArr) {
            t.Join();
        }

        watch.Stop();
        Console.WriteLine($"Spend Time: {watch.Elapsed.TotalSeconds}");
    }
    static void ExecuteThread() {
        int i = j;
        String imgName = "temp/img-" + i + ".jpg";
        DownloadImg("https://picsum.photos/200/300?random=1", imgName);
    }
    static void DownloadImg(String url, String imgName) {
		WebClient client = new WebClient();
		try {
			Console.WriteLine($"Thread {Thread.CurrentThread.Name} is downloading a img from: {url}");
			client.DownloadFile(url, imgName);
			Console.WriteLine("Image Download Succesfully!");
		} catch (InvalidCastException e) {
			Console.WriteLine("Error: " + e.Message);
		}
	}
}