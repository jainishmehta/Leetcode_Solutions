/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1==NULL && l2==NULL){
            return NULL;
        }
        ListNode *newcreated= new ListNode();
        if (l1==NULL){
            l1=newcreated;
        }
        if (l2==NULL){
            l2=newcreated;
        }
        auto *next= addTwoNumbers(l1->next, l2->next);
        ListNode* head=new ListNode(l1->val + l2->val, next);
        ListNode* temp=head;
        while (head->val>9){
            int carry=(head->val)/10;
            head->val=head->val%10;
            if (head->next==NULL){
                ListNode *node=new ListNode();
                head->next=node;
            }
            head->next->val+=carry;
            head=head->next;
        }
        head=temp;
        return head;
    }
};
