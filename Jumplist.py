from math import floor
import random
from SortedSLL import SortedSLL
from Node import Node
import graphviz 
import random

class JumpList:
    def __init__(self, sortedSLL = None):
        if sortedSLL is not None:
            self.backbone = sortedSLL
            self.build(self.backbone.head, self.backbone.n)
            # self.build_2(self.backbone.head, self.backbone.n)
            # self.build_perfect(self.backbone.head, self.backbone.n)
            # self.optimized_build(self.backbone.head, self.backbone.n)
            # self.rebalance(self.backbone.head, self.backbone.n)
            self.n = self.backbone.n
        else:
            self.backbone = SortedSLL()
            self.backbone.head = Node(-float('inf'))
            self.backbone.head.jump = self.backbone.head
            self.n = 1
            

    # def build(self, u, n):
    #     if n == 1:
    #         print('Reached base case:', u.data)
    #         return u 
    #     k = random.randint(2, n)
    #     print(f'Build call u: {u.data}, k: {k}, n: {n}')
    #     u.next_size = k-2
    #     # print('u.next_size:', u.next_size)
    #     u.jump_size = n-k+1
    #     # print('u.jump_size:', u.jump_size)
    #     p = self.build(u.next, k-1)
    #     print('Post first build call; the jump node is:', p.data)
    #     u.jump = p
    #     q = self.build(p, n-k+1)
    #     print('Post second build class; the node being returned is:', q.data)
    #     return q
    
    # def build_2(self, x, n):
    #     while(n > 1):
    #         m = random.randint(2, n)
    #         y = x.next
    #         x.next_size = m-2
    #         x.jump_size = n-m+1
    #         x.jump = self.build_2(y, m-1)
    #         # self.build(y, m-2)
    #         x = x.jump
    #         n = n-m+1
    #     return x
    
    # def build_perfect(self, x, n):
    #     while n > 1:
    #         # m = random.randint(2, n)
    #         m = floor((n-1)/2)
    #         n = n-m-1
    #         x.next_size = m
    #         x.jump_size = n
    #         y = x.next
    #         x.jump = y if m == 0 else self.build_3(y, m)
    #         x = x.jump
    #     x.jump = x
    #     x.next_size = 0
    #     x.jump_size = 0
    #     return x.next
    
    def build(self, x, n):
        while n > 1:
            m = random.randint(0, n-2)
            n = n-m-1
            x.next_size = m
            x.jump_size = n
            y = x.next
            x.jump = y if m == 0 else self.build(y, m)
            x = x.jump
        x.jump = x
        x.next_size = 0
        x.jump_size = 0
        return x.next

    # def rebalance(self, x, n):
    #     if n == 1:
    #         x.jump = None
    #         x.next_size = 0
    #         x.jump_size = 0
    #         return x.next
    #     if n == 2:
    #         x.jump = None
    #         x.next_size = 1
    #         x.jump_size = 0
    #         x.next.next_size = 0
    #         x.next.jump_size = 0
    #         return x.next.next
    #     j = random.randint(2, n)
    #     return self.set_jump_and_rebalance(x, n, j)
    
    # def set_jump_and_rebalance(self, x, n, j):
    #     nextEnd = self.rebalance(x.next, j-1)
    #     self.rebalance(nextEnd, n-j)
    #     x.jump_size = n-j+1
    #     x.next_size = j-2
    #     return x


    # def insert(self, item):
    #     self.n += 1
    #     curr = self.backbone.head
    #     while curr is not None:
    #         pred = curr
    #         if curr.next and curr.next.data >= item:
    #             curr.next_size += 1
    #             break
    #         if curr.jump and item > curr.jump.data:
    #             curr.jump_size += 1
    #             curr = curr.jump
    #         else:
    #             curr.next_size += 1
    #             curr = curr.next
    #     new_node = Node(item)
    #     new_node.next = pred.next
    #     pred.next = new_node
    #     self.restore_random_insert(self.backbone.head, self.n, new_node)


    # def restore_random_insert(self, u, n, new_node):
    #     to_rebuild = self.decision(n)
    #     print(f'to_rebuild: {to_rebuild}')
    #     if n <= 1:
    #         new_node.jump = new_node.next
    #     elif to_rebuild:
    #         self.build(u, n)
    #     elif u == new_node:
    #         u.jump = u.next
    #     elif u.jump is None:
    #         u.jump = new_node
    #     elif u.jump and u.jump.data <= new_node.data:
    #         self.restore_random_insert(u.jump, u.jump_size, new_node)
    #     elif u.next and u.next.data <= new_node.data:
    #         self.restore_random_insert(u.next, u.next_size, new_node)

    # def delete(self, item):
    #     self.n -= 1
    #     curr = self.backbone.head
    #     pred = None
    #     while curr is not None:
    #         if curr.next and curr.next.data == item:
    #             pred = curr
    #         if curr.jump and item > curr.jump.data:
    #             curr.jump_size -= 1
    #             curr = curr.jump
    #         else:
    #             curr.next_size -= 1
    #             curr = curr.next
    #     if pred is None or pred.next.data != item:
    #         print(
    #             f'Item {item} not found in the list'
    #         )
    #         return None
    #     print('pred:', pred.data, 'pred.next:', pred.next.data)
    #     pred.next = pred.next.next
    #     self.restore_random_delete(self.backbone.head, self.n, item)

    # def restore_random_delete(self, u, n, item):
    #     if u.jump and u.jump == item:
    #         self.build(u, n)
    #     elif u.jump and u.jump.data < item:
    #         self.restore_random_delete(u.jump, u.jump_size, item)
    #     else:
    #         self.restore_random_delete(u.next, u.next_size, item)

    def insert(self, item):
        self.n += 1
        pred = None
        curr = self.backbone.head
        while pred is None:
            print(curr.data)
            if curr.next and curr.next.data >= item:
                pred = curr
                pred.next_size += 1
                break
            elif curr.jump and (curr.jump is not curr) and (item > curr.jump.data):
                # print('making jump')
                curr.jump_size += 1
                curr = curr.jump
            else:
                if curr.next is None:
                    pred = curr
                    break
                curr.next_size += 1
                curr = curr.next

        new_node = Node(item)
        new_node.next = pred.next
        pred.next = new_node

        new_node.next_size = pred.next_size
        # pred.next_size += 1
        

        # print(pred.data)

        self.restore_random_insert(self.backbone.head, new_node, self.n)

    def restore_random_insert(self, u, new_node, n):
        # print('restore_random_insert called with u:', u.data, 'n:', n)
        # if n <= 1:
        #     print('restore_random_insert BASE CASE', 'u:', u.data, 'new_node:', new_node.data)
            
        to_rebuild = self.decision(n)
        if to_rebuild:
            if n <= 1:
                new_node.jump = new_node
                return
            else:
                print('rebuilding', 'u:', u.data, 'n:', n)
                self.build(u, n)
        elif u.next and u.next == new_node:
            if u.jump == u:
                print('SETTING JUMP TO NEW NODE', 'jump:', u.jump.data, 'new_node:', new_node.data)
                u.jump = new_node
                new_node.jump = new_node
                u.jump_size = 1
                u.next_size = 0
            else:
                print('restoring random and USURPING', 'next:', u.next.data, 'new_node:', new_node.data, 'next_size:', u.next_size)
                self.usurp_arches(new_node, u.next_size)
        elif u.jump.data < new_node.data:
            print('restoring random', 'JUMP:', u.jump.data, 'new_node:', new_node.data)
            self.restore_random_insert(u.jump, new_node, u.jump_size)
        elif u.next and u.next.data < new_node.data:
            print('restoring random', 'NEXT:', u.next.data, 'new_node:', new_node.data)
            self.restore_random_insert(u.next, new_node, u.next_size)
        else:
            raise Exception('Should not reach here')
    
    def usurp_arches(self, u, n):
        print('usurp_arches called with u:', u.data, 'n:', n)
        if n <= 1:
            u.jump = u
            return
        
        to_make_jump_successor = self.decision(u.next_size)
        if to_make_jump_successor:
            print('usurp: making jump successor', 'u:', u.data, 'u.next:', u.next.data)
            u.jump = u.next
            u.jump_size = u.next_size
            u.next_size = 0
        else:
            print('usurping arches', 'u:', u.data, 'u.next:', u.next.data)  
            u.next_size = u.next.next_size + 1
            u.jump_size = u.next.jump_size
            u.jump = u.next.jump
            self.usurp_arches(u.next, u.next.next_size)
        

    def decision(self, n):
        rand = random.random()
        if n == 0:
            raise Exception('n is 0')
        prob = 1/n
        # print(f'rand: {rand}, prob: {prob}')
        # return False
        return rand < prob
    

    def search(self, item):
        curr = self.backbone.head
        while curr is not None:
            print(curr.data)
            if curr.data == item:
                return curr
            if curr.jump and item >= curr.jump.data:
                print(f'making jump to {curr.jump.data}')
                curr = curr.jump
            else:
                curr = curr.next
        return None
    def search_recursive(self, item, curr):
        if curr is None:
            return None
        if curr.data == item:
            return curr
        if curr.jump and item >= curr.jump.data:
            return self.search_recursive(item, curr.jump)
        else:
            return self.search_recursive(item, curr.next)
    
    def find_predecessor(self, item):
        curr = self.backbone.head
        while curr is not None:
            if curr.next and curr.next.data >= item:
                return curr
            if curr.jump and item > curr.jump.data:
                curr = curr.jump
            else:
                curr = curr.next
        return None


    def display(self):
        curr = self.backbone.head
        while curr is not None:
            jump = curr.jump.data if curr.jump else 'NULL'
            print(f'(Val: {curr.data}, Jump: {jump}, Nsize: {curr.next_size}, Jsize: {curr.jump_size})', end="\n")
            curr = curr.next

    def create_visualization(self, filename):
        graph = graphviz.Digraph(name='jumplist', node_attr={'shape': 'rectangle'})
        graph.attr('graph', rankdir='LR')
        j = graph.subgraph(name='jumps')
        # j.attr('edge', weight='0')
        with graph.subgraph(name='backbone') as backbone, graph.subgraph(name='jumps') as jumps:
            curr = self.backbone.head
            counter = 0
            while curr is not None:
                # graph.node(name=f'node-{counter}', label=str(curr.data))
                graph.node(str(curr.data))
                if curr.next:
                    backbone.edge(str(curr.data), str(curr.next.data), weight='1', color='blue')
                    # backbone.edge(f'node-{counter}', f'node-{counter+1}', weight='1', color='blue')
                if curr.jump:
                    jumps.edge(str(curr.data), str(curr.jump.data), weight='0', color='red')
                    # jumps.edge(f'node-{counter}', f'node-{counter+curr.next_size+1}', weight='0', color='red')
                curr = curr.next
                counter += 1
        graph.render(filename, 'views', format='png', cleanup=True)

       



