#include <iostream>
#include <string>
using namespace std;

int main() {
      
   int calorieIntake;
   int numDays;
   int totalCal = 0;
   double avgCal;
   
   cout << "How many days do you want to track your calorie intake? ";
   cin >> numDays;
   for (int i = 1; i <= numDays; i++) {
      cout << "Enter calorie intake for day " << i << ": ";
      cin >> calorieIntake;
      totalCal += calorieIntake;
   }

   avgCal = static_cast<double>(totalCal) / numDays;
   cout << "Total calorie intake over " << numDays << " days: " << totalCal << endl;
   cout << "Average daily calorie intake: " << avgCal << endl;

   return 0;
}