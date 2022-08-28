using System;
using System.Diagnostics;
using System.Collections.Generic;

class Program {
    static void Main() {
        Stopwatch watch = new Stopwatch();
        Random n = new Random();

        watch.Start();
        for (int i = 0; i < 10000; i++) {
            ShowList(CalculatePrimeFactors(n.Next(20000, 100000000)));
        }

        watch.Stop();
        Console.WriteLine($"Execution Time: {watch.Elapsed.TotalSeconds}");
    }
    static List<float> CalculatePrimeFactors(int n) {

        List<float> primFac = new List<float>();

        int d = 2;

        while (d*d <= n) {
            while ((n%d) == 0) {
                primFac.Add(d);
                n = n/d;
            }
            d++;
        }
        if(n > 1) {
            primFac.Add(n);
        }
        return primFac;
    }
    static void ShowList(List<float> l) {
        String values = "";

        for (int i = 0; i < l.Count; i++) {

            if (values != "") { values = values + ","; }
            values = values + l[i];

        }

        Console.WriteLine($"[{values}]");
    }
}