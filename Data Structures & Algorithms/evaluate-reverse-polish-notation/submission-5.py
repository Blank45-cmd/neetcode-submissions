class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+','-','*','/'}
        st = []
        for token in tokens:
            if token in operators:
                right = st.pop()
                left = st.pop()
                if token =='+':
                    st.append(left+right)
                if token =='-':
                    st.append(left-right)
                if token =='/':
                    st.append(int(left/right))
                if token =='*':
                    st.append(left*right)
            else:
                st.append(int(token))
        return st.pop()
            


