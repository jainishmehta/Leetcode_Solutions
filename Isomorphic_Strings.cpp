class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mp;
        unordered_set<char> mapped; 
        
        if (s.size()!=t.size()) return false;
        for(int i=0; i<t.size(); i++){
            int s_first=s[i], t_first=t[i];
            if (mp.count(s_first)){
                if (mp[s_first]==t_first) continue;
                else return false;
            }
            else {
                if (mapped.count(t_first)) return false;
                mp[s_first]=t_first;
                mapped.insert(t_first);
            }
        }
        return true;
    }
};
