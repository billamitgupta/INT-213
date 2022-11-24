#include <iostream>
using namespace std;
void display(int *array, int size){
for(int i=0; i<size; i++){
    cout<<array[i]<<" ";
    cout<<endl;

}}
void insertSort(int *array,int size){
    int key,j;
    for (int i = 0; i < size; i++)
    {
        key = array[i];//take away
        j=i;
        while (j > 0 && array[j-1]>key)
        {
            array[j]=array[j-1];
            j--;
        }
        array[j]=key;//insert in right place
        
    }
    
}
int main(){
    int n;
    cout << "enter the number of element";
    cin>>n;
    int arr[n];  //creatr an arreay with given number of element
    cout<<"Enter the element"<<endl;
    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    cout<<"array before sorting";
    display(arr,n);
    insertSort(arr,n);
    cout<<"arrey after sorting";
    display(arr,n);
}