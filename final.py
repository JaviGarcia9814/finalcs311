from tkinter import *
from tkinter import ttk,messagebox
from ttkbootstrap import *
import numpy as np
import time


class window:
     #this window is where you press which one you want 
     start_window = {'bubble': False, 'merge': False, 'quick': False} 

     def __init__(self, root, title) -> None:
          self.root = root
          self.root.title(title)
          self.root.resizable(width=False, height=False)
          Label(self.root, text='Sorting Algorithm').grid( row=0, columnspan=6)
         
         
         
          # Buttons for the gui each sorting method has one
          self.bubblesort = ttk.Button(self.root, text='Bubble Sort', style='info.TButton', padding=5, width=15, command=self.bubble)
          self.bubblesort.grid(column=1, row=1, padx=5, pady=5)

          self.mergeSort = ttk.Button(self.root, text='Merge Sort', style='info.TButton', padding=5, width=15,command=self.merge)
          self.mergeSort.grid(column=2, row=1, padx=5, pady=5)      
            
          self.quickSort = ttk.Button(self.root, text='Quick Sort', style='info.TButton', padding=5, width=15,command=self.quick)
          self.quickSort.grid(column=3, row=1, padx=5, pady=5)  


          #buttons for to start and shuffle and the array size scalw 
          self.start = ttk.Button(self.root, text='Start', padding=5, width=15,command=self.start)
          self.start.grid(column=5, row=2, padx=5, pady=5)
          
          ttk.Button(self.root, text='Shuffle', style='info.Outline.TButton', padding=5, width=15,command=self.shuffle).grid(column=5, row=1, padx=5, pady=5)

          ttk.Label(self.root, text='Array Size:').grid(row=2,column=0)
          self.arraysize=ttk.Scale(self.root,from_=6,to=100,length=100,style='success.Horizontal.TScale',value=10,command=lambda x:self.slide_function())
          self.arraysize.grid(row=2,column=1,columnspan=3)
         
         
         
          #this is where the rectangle will show up and where they are drawn on the canvas 
          self.canvas=Canvas(self.root, width=800-5, height=400,highlightbackground="white",highlightthickness=2,bg='white')
          self.canvas.grid(row=4, padx=5, pady=10, columnspan=6)



          
          self.speed = .5
          self.N =5
          self.colours =['dodgerblue' for index_f in range(self.N)]
          N=self.N
          self.data = np.linspace(2,200,N,dtype=np.uint16)
          np.random.shuffle(self.data)
          self.display(N,self.data,self.colours)
        
     
     #will diplay the recatangles 
     def display(self,N: int,arr: list,color_of_rec: list):

          self.canvas.delete('all')
          width = (1570)/(3*N-1)
          gap = width/2


          for index_f in range(N): self.canvas.create_rectangle(7+index_f*width+index_f*gap,0,7+(index_f+1)*width+index_f*gap,arr[index_f],fill=color_of_rec[index_f])

          self.root.update_idletasks()

     #slide fundtion 
     def slide_function(self):
          self.N = int(self.arraysize.get())
          self.data = np.linspace(5,400,self.N,dtype=np.uint16)
          self.speed = 5/self.arraysize.get()
          self.colours = ['dodgerblue' for _ in range(self.N)]
          self.shuffle()
          
     #shuffle the rectangles around using random libray 
     def shuffle(self):
          self.canvas.delete('all')
          self.data = np.linspace(5,400,self.N,dtype=np.uint16)
          np.random.shuffle(self.data)
          self.display(self.N,self.data,self.colours)


     # button selection of sorting 
     def bubble(self):
          if self.start_window['bubble'] is False:
               self.start_window['bubble'] = True
               self.bubblesort.config(style = 'success.TButton')

               for index_f in self.start_window:
                    if index_f != 'bubble': self.start_window[index_f] = False

               self.quickSort.config(style = 'info.TButton')               
               self.mergeSort.config(style = 'info.TButton')
              
          else:
               self.start_window['bubble'] = False
               self.bubblesort.config(style ='info.TButton')
               

     def merge(self):
          if self.start_window['merge'] is False:
               self.start_window['merge'] = True
               self.mergeSort.config(style = 'success.TButton')

               for index_f in self.start_window:
                    if index_f != 'merge': self.start_window[index_f] = False

               self.quickSort.config(style='info.TButton')               
               self.bubblesort.config(style='info.TButton')
          
               
          else:
               self.start_window['merge'] = False
               self.mergeSort.config(style='info.TButton')
               

     def quick(self):
          if self.start_window['quick'] is False:
               self.start_window['quick'] = True
               self.quickSort.config(style='success.TButton')

               for index_f in self.start_window:
                    if index_f != 'quick': self.start_window[index_f]=False

               self.mergeSort.config(style='info.TButton')               
               self.bubblesort.config(style='info.TButton')
          else:
               self.start_window['quick'] = False
               self.quickSort.config(style='info.TButton')
               

     
 
     
     def start(self):
          if self.start_window['bubble'] is True:
               for index_f in range(self.N-1):
                    for index_b in range(self.N-1-index_f):
                         self.display(self.N,self.data,['purple' if arr==index_b or arr==index_b+1 else 'green' if arr>self.N-1-index_f else 'dodgerblue' for arr in range(self.N)])
                         time.sleep(self.speed)
                         if self.data[index_b]>self.data[index_b+1]:
                              self.display(self.N,self.data,['red' if arr==index_b or arr==index_b+1 else 'green' if arr>self.N-1-index_f else 'dodgerblue' for arr in range(self.N)])
                              time.sleep(self.speed)
                              self.data[index_b],self.data[index_b+1]=self.data[index_b+1],self.data[index_b]
                              self.display(self.N,self.data,['lime' if arr==index_b or arr==index_b+1 else 'green' if arr>self.N-1-index_f else 'dodgerblue' for arr in range(self.N)])
                              time.sleep(self.speed)
               self.display(self.N,self.data,['lime' for _ in range(self.N)])
               

          elif self.start_window['merge'] is True:
               self.mergesort(self.data,0,self.N-1)
               self.display(self.N,self.data,['lime' for _ in range(self.N)])

          elif self.start_window['quick'] is True:
               self.quicksort(self.data,0,self.N-1)
               self.display(self.N,self.data,['lime' for _ in range(self.N)])

          else:
               #show messege box
               messagebox.showerror("Algorithm Visualizer", "You didn't select any sorting algorithm")
               

     #merge sort algothrim 

     def mergesort(self,arr,front,last):
          if front<last:
               mid= (front+last)//2

               self.mergesort(arr,front,mid)
               self.mergesort(arr,mid+1,last)


               self.display(self.N,self.data,['dodgerblue' for _ in range(self.N)])
               
               rj=mid+1
               if arr[mid]<=arr[mid+1]:
                    return 
               
               while front<=mid and rj<=last:
                    self.display(self.N,self.data,['yellow' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                    time.sleep(self.speed)
                    if arr[front]<=arr[rj]:
                         self.display(self.N,self.data,['lime' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                         time.sleep(self.speed)
                         front+=1
                    else:
                         self.display(self.N,self.data,['red' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                         time.sleep(self.speed)
                         temp=arr[rj]
                         index_f=rj
                         while index_f!=front:
                              arr[index_f]=arr[index_f-1]
                              index_f-=1
                         arr[front]=temp
                         self.display(self.N,self.data,['lime' if x==front or x==rj else 'dodgerblue' for x in range(self.N)])
                         time.sleep(self.speed)

                         front+=1
                         mid+=1
                         rj+=1
          
               self.display(self.N,self.data,['dodgerblue' for _ in range(self.N)])
               time.sleep(self.speed)
     
     #quick sort algorthrim 
     def partition(self,arr,index_f,index_b):

          l=index_f 

          pivot=arr[index_f]
          piv_index=index_f

          while index_f<index_b:
               while  index_f<len(arr) and arr[index_f]<= pivot:
                    index_f+=1
                    self.display(self.N,self.data,['purple' if x==piv_index else 'yellow' if x==index_f else "dodgerblue" for x in range(self.N)])
                    time.sleep(self.speed)
               while arr[index_b]>pivot:
                    index_b-=1
               if index_f<index_b:
                    self.display(self.N,self.data,['red' if x==index_f or x==index_b else "dodgerblue" for x in range(self.N)])
                    time.sleep(self.speed)
                    arr[index_f],arr[index_b]=arr[index_b],arr[index_f]
                    self.display(self.N,self.data,['lime' if x==index_f or x==index_b else "dodgerblue" for x in range(self.N)])
                    time.sleep(self.speed)
          arr[index_b],arr[l]=arr[l],arr[index_b]
          return index_b

     #quicksort 
     def quicksort(self,arr,index_f,index_b):
          if index_f<index_b:
               x=self.partition(arr,index_f,index_b)
          
               self.quicksort(arr,index_f,x-1)
               self.quicksort(arr,x+1,index_b)
  
#main will run the fuction    
if __name__ == '__main__':
     win = Style(theme = 'minty').master
     obj = window(win, 'final project')

     win.mainloop()
