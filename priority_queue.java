Queue<Integer> minimumCostHeap = new PriorityQueue<>();
for(int n: A)
    minimumCostHeap.offer(n);
int result = 0;
while(minimumCostHeap.size() > 1) {
    int first = minimumCostHeap.poll();
    int second = minimumCostHeap.poll();
    int summation = first + second;
    result += summation;
    minimumCostHeap.offer(summation);
}
return result;
    