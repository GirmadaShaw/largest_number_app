import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers to find the largest among them:")

    a = st.number_input("Enter the first number:", value=0)
    b = st.number_input("Enter the second number:", value=0)
    c = st.number_input("Enter the third number:", value=0)

    if st.button("Find Largest"):
        largest = find_largest_number(a, b, c)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
