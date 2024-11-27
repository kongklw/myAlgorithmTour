'''
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        '''
        思路：因为要求O(m+n)也就是说需要遍历一趟。
            既然这样，先遍历到m列表，把大的数据全部放到n 的列表中。然后遍历完了m以后呢，把剩下的全部跟0交换。
            
        思路2：
            最先想到的是小的开始排序。 问题是，小的在前面需要交换顺序。反向思考，大的放后面。
        '''
        # p1, p2 = m - 1, n - 1
        # tail = m + n - 1
        # while p1 >= 0 or p2 >= 0:
        #     print('this time values are : ',p1,p2)
        #     if p1 == -1:
        #         print('haha p1')
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     elif p2 == -1:
        #         print('haha p2')
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     elif nums1[p1] > nums2[p2]:
        #         nums1[tail] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[tail] = nums2[p2]
        #         p2 -= 1
        #     tail -= 1



        cur1 = m - 1
        cur2 = n - 1
        for i in range(m + n - 1, 0, -1):
            if cur1 < 0 or cur2 < 0:
                break
            if nums1[cur1] < nums2[cur2]:
                nums1[i] = nums2[cur2]
                cur2 -= 1

            else:
                nums1[i] = nums1[cur1]
                cur1 -= 1


if __name__ == '__main__':
    s = Solution()
    # nums1 = [1, 2, 3,7,9, 0, 0, 0]
    nums1 = [0]

    m = 0
    nums2 = [1]
    n = 1


    s.merge(nums1, m, nums2, n)
    print(nums1)
