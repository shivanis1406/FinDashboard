import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
import plotly.graph_objs as go
from news_analyzer import get_news_analysis

# Dummy Data Generator
class DummyDataGenerator:
    @staticmethod
    def generate_financial_timeseries():
        # Generate quarterly financial data
        quarters = ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 
                    'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
        
        revenue = np.cumsum(np.random.normal(500, 100, len(quarters))) + 5000
        net_profit = np.cumsum(np.random.normal(100, 50, len(quarters))) + 1000
        
        return pd.DataFrame({
            'Quarter': quarters,
            'Revenue (₹ Cr)': revenue,
            'Net Profit (₹ Cr)': net_profit
        })
    
    @staticmethod
    def generate_financial_summary():
        return {
            'Revenue': f"₹{random.randint(1000, 5000)} Crore",
            'Net Profit': f"₹{random.randint(100, 500)} Crore",
            'Market Cap': f"₹{random.randint(10000, 50000)} Crore",
            'EPS': round(random.uniform(10, 50), 2),
            'P/E Ratio': round(random.uniform(20, 50), 2),
            'ROE (%)': round(random.uniform(10, 25), 2)
        }
    
    @staticmethod
    def generate_document_corpus():
        return [
            {
                'type': 'Annual Report 2023',
                'source': 'Company Filing',
                'content': """Zomato Limited has demonstrated significant growth in the food delivery ecosystem. 
                Our technological innovations and strategic partnerships have been key drivers of our expansion. 
                We continue to focus on improving user experience, expanding restaurant networks, and leveraging 
                data-driven insights to optimize our platform."""
            },
            {
                'type': 'Q4 Earnings Call Transcript',
                'source': 'Company Earnings',
                'content': """Our Q4 performance reflects the robust growth in the food delivery market. 
                We've seen a 35% increase in order volumes and improved unit economics. 
                Our investments in technology and logistics have been critical to our success."""
            },
            {
                'type': 'Economic Times News',
                'source': 'News Article',
                'content': """Zomato is exploring expansion into quick commerce and grocery delivery. 
                The company sees significant potential in diversifying its service offerings beyond 
                traditional restaurant delivery."""
            },
            {
                'type': 'Sustainability Report',
                'source': 'ESG Reporting',
                'content': """We are committed to reducing our carbon footprint. Our delivery fleet 
                is progressively moving towards electric vehicles, and we've implemented sustainable 
                packaging solutions across our restaurant partners."""
            },
            {
                'type': 'Expert Interview',
                'source': 'CNBC YouTube',
                'content': """The food delivery market in India is evolving rapidly. Zomato's strategic 
                approach to technology, user experience, and restaurant partnerships positions it 
                uniquely in this competitive landscape."""
            }
        ]

def main():
    st.set_page_config(page_title="Zomato Information Dashboard", layout="wide")
    
    # Sidebar for Navigation
    st.sidebar.title("Zomato Information Hub")
    menu = st.sidebar.radio(
        "Select Section", 
        ["Financial Summary", "Ask Me Anything", "Company Overview", "Sectoral Analysis"]
    )
    
    # Financial Summary Section
    if menu == "Financial Summary":
        st.title("Zomato - Financial Performance")
        
        # Generate Financial Data
        financial_summary = DummyDataGenerator.generate_financial_summary()
        financial_timeseries = DummyDataGenerator.generate_financial_timeseries()
        
        # Financial Metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Revenue", financial_summary['Revenue'])
            st.metric("Market Cap", financial_summary['Market Cap'])
        
        with col2:
            st.metric("Net Profit", financial_summary['Net Profit'])
            st.metric("EPS", financial_summary['EPS'])
        
        with col3:
            st.metric("P/E Ratio", financial_summary['P/E Ratio'])
            st.metric("ROE", f"{financial_summary['ROE (%)']}%")
        
        # Plots
        st.subheader("Quarterly Financial Trends")
        
        # Revenue Line Chart
        fig_revenue = px.line(
            financial_timeseries, 
            x='Quarter', 
            y='Revenue (₹ Cr)', 
            title='Quarterly Revenue Trend',
            labels={'Revenue (₹ Cr)': 'Revenue (₹ Crore)'}
        )
        st.plotly_chart(fig_revenue, use_container_width=True)
        
        # Profit Line Chart
        fig_profit = px.line(
            financial_timeseries, 
            x='Quarter', 
            y='Net Profit (₹ Cr)', 
            title='Quarterly Net Profit Trend',
            labels={'Net Profit (₹ Cr)': 'Net Profit (₹ Crore)'}
        )
        st.plotly_chart(fig_profit, use_container_width=True)
    
    # Ask Me Anything Section
    elif menu == "Ask Me Anything":
        st.title("Information Discovery")
        
        # Search Input
        search_query = st.text_input("Enter a keyword to search across company documents")
        
        if search_query:
            # Generate document corpus
            documents = DummyDataGenerator.generate_document_corpus()
            
            # Search and display results
            st.subheader(f"Search Results for '{search_query}'")
            
            # Track number of matches
            match_count = 0
            
            for doc in documents:
                # Case-insensitive search
                if search_query.lower() in doc['content'].lower():
                    match_count += 1
                    
                    # Create an expander for each result
                    with st.expander(f"{doc['type']} - {doc['source']}"):
                        # Highlight the search term
                        highlighted_content = doc['content'].replace(
                            search_query, 
                            f"**{search_query}**"
                        )
                        st.markdown(highlighted_content)
            
            # Display match information
            if match_count == 0:
                st.info("No results found. Try a different keyword.")
            else:
                st.success(f"Found {match_count} matching document{'s' if match_count > 1 else ''}")
    
    # Company Overview Section
    elif menu == "Company Overview":
        st.title("Zomato - Company Overview")
        
        # Company Basics
        st.header("Company Snapshot")
        overview_cols = st.columns(2)
        
        with overview_cols[0]:
            st.markdown("""
            **Founding Year:** 2010
            **Headquarters:** Bangalore, India
            **Founders:** Deepinder Goyal, Pankaj Chaddah
            **Industry:** Food Delivery, Restaurant Discovery
            """)
        
        with overview_cols[1]:
            st.markdown("""
            **Business Model:** 
            - Food Delivery Platform
            - Restaurant Marketplace
            - Cloud Kitchen Services
            - Dining Out Recommendations
            """)
        
        # Key Milestones
        st.header("Key Milestones")
        milestones = [
            "2010: Founded as a restaurant discovery platform",
            "2015: Launched food delivery services",
            "2021: Successful IPO on NSE and BSE",
            "2023: Expanded to 500+ cities in India"
        ]
        
        for milestone in milestones:
            st.markdown(f"- {milestone}")
    
    # New Sectoral Analysis Section
    elif menu == "Sectoral Analysis":        
        # Call get_news_analysis function with parameter 1
        try:
            get_news_analysis(0)     
        except Exception as e:
            st.error(f"Error fetching sectoral analysis: {e}")
            st.info("Please ensure the news_analyzer module is correctly implemented.")


if __name__ == "__main__":
    main()
