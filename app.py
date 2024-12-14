import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime, timedelta

class ZomatoDashboard:
    def __init__(self):
        # Simulated data sources (would be replaced with actual data retrieval methods)
        self.financial_data = self._load_financial_data()
        self.news_data = self._load_news_data()
        self.expert_insights = self._load_expert_insights()
        self.regulatory_filings = self._load_regulatory_filings()

    def _load_financial_data(self):
        # Simulated financial data from annual/quarterly reports
        return pd.DataFrame({
            'Year': [2021, 2022, 2023],
            'Revenue': [1200, 1800, 2500],
            'Net Profit': [50, 120, 200],
            'Margin (%)': [4.2, 6.7, 8.0]
        })

    def _load_news_data(self):
        # Simulated news sentiment analysis
        return pd.DataFrame({
            'Date': pd.date_range(end=datetime.now(), periods=30),
            'Sentiment': ['Positive', 'Neutral', 'Negative'] * 10,
            'Headline': [
                f"Zomato Expands to New Market {i}" for i in range(30)
            ]
        })

    def _load_expert_insights(self):
        # Simulated expert interview insights
        return [
            {
                'Expert': 'Financial Analyst A',
                'Insight': 'Strong growth potential in food delivery market',
                'Confidence': 'High'
            },
            {
                'Expert': 'Industry Expert B',
                'Insight': 'Challenges in profitability and market competition',
                'Confidence': 'Medium'
            }
        ]

    def _load_regulatory_filings(self):
        # Simulated regulatory filing summaries
        return {
            'Latest Annual Report': '2023 financial performance shows significant growth',
            'Key Regulatory Highlights': [
                'Expansion of restaurant partnerships',
                'Investment in technology infrastructure',
                'Compliance with new e-commerce regulations'
            ]
        }

    def render_dashboard(self):
        st.title('Zomato Comprehensive Insights Dashboard')
        
        # Sidebar for data source navigation
        st.sidebar.title('Data Sources')
        source_options = [
            'Financial Overview', 
            'News Sentiment', 
            'Expert Insights', 
            'Regulatory Filings'
        ]
        selected_source = st.sidebar.radio('Select Information Source', source_options)

        # Dynamic content rendering
        if selected_source == 'Financial Overview':
            self._render_financial_section()
        elif selected_source == 'News Sentiment':
            self._render_news_sentiment_section()
        elif selected_source == 'Expert Insights':
            self._render_expert_insights_section()
        else:
            self._render_regulatory_section()

    def _render_financial_section(self):
        st.header('Financial Performance')
        
        # Revenue and Profit Chart
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=self.financial_data['Year'], 
            y=self.financial_data['Revenue'], 
            name='Revenue',
            marker_color='blue'
        ))
        fig.add_trace(go.Bar(
            x=self.financial_data['Year'], 
            y=self.financial_data['Net Profit'], 
            name='Net Profit',
            marker_color='green'
        ))
        fig.update_layout(title='Annual Revenue and Profit Trend')
        st.plotly_chart(fig)

        # Margin Analysis
        col1, col2 = st.columns(2)
        with col1:
            st.metric('Latest Margin', f"{self.financial_data['Margin (%)'].iloc[-1]}%")
        with col2:
            st.metric('Revenue Growth', f"{self.financial_data['Revenue'].pct_change().iloc[-1]*100:.2f}%")

    def _render_news_sentiment_section(self):
        st.header('News Sentiment Analysis')
        
        # Sentiment Distribution
        sentiment_counts = self.news_data['Sentiment'].value_counts()
        fig = px.pie(
            values=sentiment_counts.values, 
            names=sentiment_counts.index, 
            title='News Sentiment Distribution'
        )
        st.plotly_chart(fig)

        # Recent Headlines
        st.subheader('Recent Headlines')
        for _, row in self.news_data.sample(5).iterrows():
            st.write(f"- {row['Headline']} (Sentiment: {row['Sentiment']})")

    def _render_expert_insights_section(self):
        st.header('Expert Insights')
        
        for insight in self.expert_insights:
            st.markdown(f"""
            **{insight['Expert']}**
            - *Insight*: {insight['Insight']}
            - *Confidence Level*: {insight['Confidence']}
            """)

    def _render_regulatory_section(self):
        st.header('Regulatory Filings & Compliance')
        
        st.subheader('Latest Annual Report Summary')
        st.write(self.regulatory_filings['Latest Annual Report'])

        st.subheader('Key Regulatory Highlights')
        for highlight in self.regulatory_filings['Key Regulatory Highlights']:
            st.write(f"- {highlight}")

def main():
    dashboard = ZomatoDashboard()
    dashboard.render_dashboard()

if __name__ == "__main__":
    main()
