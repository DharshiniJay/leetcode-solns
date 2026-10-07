class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector <int> b;   
        int x;
   
                for(int k=0;k<nums1.size();k++){   
                     bool found =false;  
                    for(int i=0;i<nums2.size();i++){
                        if(nums1[k]==nums2[i]) {
                            x=i;
                            for (int j = i + 1; j < nums2.size(); j++) {
                                if (nums2[j] > nums2[i]) {
                                b.push_back(nums2[j]);
                                found = true;
                                break;
                                }
                            }
                        }                        
                    }
                    if(!found){
                       b.push_back(-1);
                    }
                }
        return b;
    }
};