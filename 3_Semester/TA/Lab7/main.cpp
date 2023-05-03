#include <iostream>

using namespace std

struct point {
	int x, y;
};










main() {
	int n, i, j;
	point p, p0;
	point* points;
	cout<<"Input number of points:"
	cin >> n;
	points = new point[n];
	for (i = 0; i < n; i++) {
		cout << "Input x and y point #" << i+1;
		cin >> points[i].x;
		cin >> points[i].y;
	}
	cout << points[2].x;


}