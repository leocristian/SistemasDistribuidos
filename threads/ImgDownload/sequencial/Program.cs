
using System;
using System.Net;
using System.Diagnostics;

namespace download_img_sequential;
class Program {
	static void Main() {
		
		String imgName, url;
		Stopwatch watch = new Stopwatch();

		url = "https://picsum.photos/200/300?random=1";

		watch.Start();
		for (int i=0;i<10;i++) {
			imgName = "./temp/img-" + i.ToString() + ".jpg";
			DownloadImg(url, imgName);
		}
		watch.Stop();
		Console.WriteLine($"Spend Time: {watch.Elapsed.TotalSeconds}");
	}
	static void DownloadImg(String url, String imgName) {

		WebClient client = new WebClient();
		
        try {
			Console.WriteLine($"Downloading Img from: {url}");
			client.DownloadFile("https://picsum.photos/200/300?random=1", imgName);
			Console.WriteLine("Image Download Succesfully!");
		} catch (InvalidCastException e) {
			Console.WriteLine("Error: " + e.Message);
		}
	}
}
