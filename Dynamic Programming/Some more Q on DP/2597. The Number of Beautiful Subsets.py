# Method 1: Backtracking

"""

class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        Set<Integer> visited = new HashSet<>();
        return backtrack(nums, k, 0, visited);
    }

    private int backtrack(int[] nums, int k, int i, Set<Integer> visited) {
        if (i == nums.length) {
            return visited.size() > 0 ? 1 : 0;
        }
        int ans = backtrack(nums, k, i + 1, visited);
        if (!visited.contains(nums[i] - k)) {
            visited.add(nums[i]);
            ans += backtrack(nums, k, i + 1, visited);
            visited.remove(nums[i]);
        }
        return ans;
    }
}

"""

# same above logic is not working in python
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        visited = set()
        n = len(nums)

        def backtrack(i, visited):
            if i  == n:
                return 1 if len(visited) > 0 else 0
            ans = backtrack(i +1, visited)
            if (nums[i] - k) not in visited:
                visited.add(nums[i])
                ans += backtrack(i +1, visited)
                visited.remove(nums[i])
            return ans
        return backtrack(0, visited)
        

# Method 2: Using DP
# Logic: 1) Group all elements a/c to remainder 'num % k'.
# Elements of one group won't affect ans of other group.
# 2) Now traverse each group and find ans of each group.
# Note: Note we can multiply answer of each group since together they will form 'm*n' subsets. (m = no of subsets in one gr and n = no of subsets in 2nd group).
# 3) How to find anser of each group.
# sort the elements of that gr so that we only need to compare with prev element only.
# find the frequency of element in that group.
# a) Then traverse frequency map.
# b) for each element no of subsets generated by himself = pow(2, freq) - 1  , '1' for : empty 
# c) We have two case(prev element has diffenec = k, prev element has difference != k) and 
# two option inside each case(when you don't take cur ele , when you take cur element).

# Now see the code to understand .

# Link: in sheet

class Solution:
    def beautifulSubsets(self, nums, k):
        mp = defaultdict(list)
        for el in nums:
            mp[el % k].append(el)
        ans = 1
        
        for mod_cal, v in mp.items():
            v.sort()
            mp2 = defaultdict(int)
            for el in v:
                mp2[el] += 1
            
            prev_el = float('-inf')
            prevNotTaken = 1
            prevTaken = 0
            nowNotTaken = 0
            nowTaken = 0
            
            for el, freq in mp2.items():
                poss_subsets = pow(2, freq) - 1  # no of subsets that will be formed by 'el' . all indexes are considered different so duplicate subset will be also there
                
                if prev_el + k == el:
                    # if pre_ele has diff = k then
                    nowNotTaken = prevNotTaken + prevTaken   # it will carry only the no of subsets oof prev one
                    nowTaken = prevNotTaken * poss_subsets   # we can multiply(union) with prevNotTaken because we can't take the pre_ele so we will have to use 
                                                            # the case when prev_ele was not taken.
                else:
                    nowNotTaken = prevNotTaken + prevTaken  # same as above
                    nowTaken = (prevNotTaken + prevTaken) * poss_subsets  # Here we can take both subsets when pre_ele was not taken & when prev_ele was taken.
                prevNotTaken = nowNotTaken
                prevTaken = nowTaken
                prev_el = el
            
            ans *= (nowNotTaken + nowTaken)   # multiply ans of each group to ans till now
        
        return ans - 1   # '-1' for empty subset
    

# Later do in O(n) using Neetcode video.
# By reducing the problem to 'House Robber' problem.
# Link: https://www.youtube.com/watch?v=Dle_SpjHTio&pp=ygUodGhlIG51bWJlciBvZiBiZWF1dGlmdWwgc3Vic2V0cyBsZWV0Y29kZQ%3D%3D