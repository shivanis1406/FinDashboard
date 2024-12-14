import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime, timedelta

class ZomatoDashboard:
    def __init__(self):
        # Expanded financial data
        self.financial_data = self._load_financial_data()
        self.segment_revenue = self._load_segment_revenue()
        self.quarterly_performance = self._load_quarterly_performance()
        
        # Social media sentiment
        self.social_media_sentiment = self._load_social_media_sentiment()
        
        # Expert interviews
        self.expert_interviews = self._load_expert_interviews()

        # News analysis
        self.news_analysis = self._load_news_analysis()

    def _load_financial_data(self):
        # More comprehensive financial data
        return pd.DataFrame({
            'Year': [2021, 2022, 2023],
            'Revenue': [1200, 1800, 2500],
            'Net Profit': [50, 120, 200],
            'Margin (%)': [4.2, 6.7, 8.0],
            'EBITDA': [180, 280, 400],
            'Operating Expenses': [1020, 1520, 2100],
            'Cash Reserves': [500, 650, 850]
        })

    def _load_segment_revenue(self):
        # Revenue breakdown by segment
        return pd.DataFrame({
            'Segment': ['Food Delivery', 'Dining Out', 'Product Sales', 'Others'],
            'Revenue (₹ Cr)': [1500, 600, 250, 150],
            'Growth (%)': [35, 20, 15, 5]
        })

    def _load_quarterly_performance(self):
        # Quarterly financial performance
        return pd.DataFrame({
            'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023'],
            'Revenue': [600, 650, 700, 750],
            'Net Profit': [50, 55, 60, 65],
            'Margin (%)': [8.3, 8.5, 8.6, 8.7]
        })

    def _load_social_media_sentiment(self):
        # Social media sentiment analysis
        return {
            'overall_sentiment': {
                'Positive': 45,
                'Neutral': 35,
                'Negative': 20
            },
            'top_posts': [
                {
                    'Platform': 'Twitter',
                    'Content': 'Zomato\'s new grocery delivery service looks promising!',
                    'Likes': 2500,
                    'Retweets': 450,
                    'Sentiment': 'Positive'
                },
                {
                    'Platform': 'Instagram',
                    'Content': 'Fast food delivery getting faster with Zomato\'s tech upgrades',
                    'Likes': 3200,
                    'Comments': 120,
                    'Sentiment': 'Positive'
                },
                {
                    'Platform': 'Twitter',
                    'Content': 'Concerns about rising delivery charges',
                    'Likes': 1800,
                    'Retweets': 250,
                    'Sentiment': 'Negative'
                }
            ]
        }

    def _load_expert_interviews(self):
        # Expert interviews with detailed insights
        return [
            {
                'Expert': 'Rajesh Sharma, Tech Analyst',
                'Channel': 'CNBC India',
                'YouTube URL': 'https://www.youtube.com/example1',
                'Key Insights': [
                    {
                        'Timestamp': '5:30',
                        'Insight': 'Zomato\'s AI-driven logistics optimization',
                        'Significance': 'High potential for cost reduction'
                    },
                    {
                        'Timestamp': '12:45',
                        'Insight': 'International expansion strategy',
                        'Significance': 'Critical for long-term growth'
                    }
                ],
                'Overall Assessment': 'Bullish on Zomato\'s technological innovations'
            },
            {
                'Expert': 'Priya Iyer, Financial Analyst',
                'Channel': 'ET Now',
                'YouTube URL': 'https://www.youtube.com/example2',
                'Key Insights': [
                    {
                        'Timestamp': '7:15',
                        'Insight': 'Profitability improvement in core business',
                        'Significance': 'Positive signal for investors'
                    },
                    {
                        'Timestamp': '18:20',
                        'Insight': 'Potential strategic partnerships',
                        'Significance': 'Could drive future growth'
                    }
                ],
                'Overall Assessment': 'Cautiously optimistic about future prospects'
            }
        ]

    def _load_news_analysis(self):
        # Comprehensive news analysis data
        return {
            'overall_sentiment': {
                'Positive': 40,
                'Neutral': 35,
                'Negative': 25
            },
            'news_sources': [
                'Economic Times',
                'Financial Express',
                'Business Standard',
                'NDTV Profit'
            ],
            'key_news_stories': [
                {
                    'Title': 'Zomato Expands Grocery Delivery Service',
                    'Source': 'Economic Times',
                    'Date': '2023-12-10',
                    'Sentiment': 'Positive',
                    'Summary': 'Zomato launches comprehensive grocery delivery platform, targeting 50 major cities',
                    'Impact': 'High potential for revenue diversification'
                },
                {
                    'Title': 'Zomato Invests in AI-Driven Logistics',
                    'Source': 'Financial Express',
                    'Date': '2023-11-25',
                    'Sentiment': 'Positive',
                    'Summary': 'Company announces significant investment in AI technology to optimize delivery routes',
                    'Impact': 'Expected cost reduction and efficiency improvement'
                },
                {
                    'Title': 'Challenges in Profitability Persist',
                    'Source': 'Business Standard',
                    'Date': '2023-11-15',
                    'Sentiment': 'Negative',
                    'Summary': 'Ongoing competition and high operational costs challenge Zomato\'s path to profitability',
                    'Impact': 'Potential investor concern'
                }
            ],
            'news_trend_analysis': pd.DataFrame({
                'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                'Positive Mentions': [30, 35, 40, 45, 50, 55],
                'Negative Mentions': [20, 18, 25, 22, 20, 15]
            }),
            'keyword_frequency': {
                'Technology': 45,
                'Expansion': 35,
                'Profitability': 30,
                'Competition': 25,
                'Innovation': 20
            }
        }

    def render_dashboard(self):
        st.title('Zomato Comprehensive Investor Dashboard')
        
        # Sidebar for navigation
        st.sidebar.title('Dashboard Sections')
        section_options = [
            'Financial Deep Dive', 
            'Social Media Pulse', 
            'Expert Interview Insights', 
            'Segment Analysis',
            'News Analysis'  # New section added
        ]
        selected_section = st.sidebar.radio('Navigate Sections', section_options)

        # Dynamic content rendering
        if selected_section == 'Financial Deep Dive':
            self._render_financial_deep_dive()
        elif selected_section == 'Social Media Pulse':
            self._render_social_media_section()
        elif selected_section == 'Expert Interview Insights':
            self._render_expert_interviews_section()
        elif selected_section == 'Segment Analysis':
            self._render_segment_analysis()
        else:
            self._render_news_analysis_section()

    def _render_financial_deep_dive(self):
        st.header('Financial Performance Analysis')
        
        # Comprehensive Financial Overview
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('Total Revenue (₹ Cr)', f"{self.financial_data['Revenue'].iloc[-1]}")
        with col2:
            st.metric('Net Profit (₹ Cr)', f"{self.financial_data['Net Profit'].iloc[-1]}")
        with col3:
            st.metric('Profit Margin', f"{self.financial_data['Margin (%)'].iloc[-1]}%")

        # Quarterly Performance Chart
        st.subheader('Quarterly Performance Trend')
        fig_quarterly = go.Figure()
        fig_quarterly.add_trace(go.Bar(
            x=self.quarterly_performance['Quarter'], 
            y=self.quarterly_performance['Revenue'], 
            name='Revenue',
            marker_color='blue'
        ))
        fig_quarterly.add_trace(go.Line(
            x=self.quarterly_performance['Quarter'], 
            y=self.quarterly_performance['Net Profit'], 
            name='Net Profit',
            marker_color='green',
            yaxis='y2'
        ))
        fig_quarterly.update_layout(
            title='Quarterly Revenue and Profit Progression',
            yaxis=dict(title='Revenue (₹ Cr)'),
            yaxis2=dict(title='Net Profit (₹ Cr)', overlaying='y', side='right')
        )
        st.plotly_chart(fig_quarterly)

        # Key Financial Ratios
        st.subheader('Key Financial Indicators')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric('EBITDA (₹ Cr)', f"{self.financial_data['EBITDA'].iloc[-1]}")
        with col2:
            st.metric('Operating Expenses (₹ Cr)', f"{self.financial_data['Operating Expenses'].iloc[-1]}")
        with col3:
            st.metric('Cash Reserves (₹ Cr)', f"{self.financial_data['Cash Reserves'].iloc[-1]}")

    def _render_social_media_section(self):
        st.header('Social Media Sentiment Analysis')
        
        # Sentiment Distribution
        st.subheader('Overall Social Media Sentiment')
        sentiment_data = self.social_media_sentiment['overall_sentiment']
        fig_sentiment = px.pie(
            values=list(sentiment_data.values()), 
            names=list(sentiment_data.keys()), 
            title='Social Media Sentiment Breakdown'
        )
        st.plotly_chart(fig_sentiment)

        # Top Social Media Posts
        st.subheader('Influential Social Media Posts')
        for post in self.social_media_sentiment['top_posts']:
            st.markdown(f"""
            **{post['Platform']} Post**
            - *Content*: {post['Content']}
            - *Engagement*: {post.get('Likes', 'N/A')} Likes, {post.get('Retweets', post.get('Comments', 'N/A'))} {post.get('Retweets') and 'Retweets' or 'Comments'}
            - *Sentiment*: {post['Sentiment']}
            """)

    def _render_expert_interviews_section(self):
        st.header('Expert Interview Insights')
        
        for interview in self.expert_interviews:
            st.markdown(f"""
            ### {interview['Expert']} - {interview['Channel']}
            **Interview Link**: [{interview['YouTube URL']}]({interview['YouTube URL']})
            
            **Key Insights:**
            """)
            
            for insight in interview['Key Insights']:
                st.markdown(f"""
                - **Timestamp {insight['Timestamp']}**: {insight['Insight']}
                  *Significance*: {insight['Significance']}
                """)
            
            st.markdown(f"**Overall Assessment**: *{interview['Overall Assessment']}*")
            st.markdown("---")

    def _render_segment_analysis(self):
        st.header('Revenue Segment Analysis')
        
        # Segment Revenue Breakdown
        fig_segment = px.bar(
            self.segment_revenue, 
            x='Segment', 
            y='Revenue (₹ Cr)', 
            text='Growth (%)',
            title='Revenue Breakdown by Business Segment'
        )
        fig_segment.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig_segment)

        # Detailed Segment Insights
        st.subheader('Segment Performance Insights')
        for _, segment in self.segment_revenue.iterrows():
            st.markdown(f"""
            **{segment['Segment']}**:
            - Revenue: ₹{segment['Revenue (₹ Cr)']} Crores
            - Growth: {segment['Growth (%)']}%
            """)

    def _render_news_analysis_section(self):
        st.header('Comprehensive News Analysis')
        
        # Overall News Sentiment
        st.subheader('News Sentiment Distribution')
        sentiment_data = self.news_analysis['overall_sentiment']
        fig_sentiment = px.pie(
            values=list(sentiment_data.values()), 
            names=list(sentiment_data.keys()), 
            title='News Sentiment Breakdown'
        )
        st.plotly_chart(fig_sentiment)

        # News Trend Analysis
        st.subheader('News Sentiment Trend')
        trend_data = self.news_analysis['news_trend_analysis']
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=trend_data['Month'], 
            y=trend_data['Positive Mentions'], 
            mode='lines+markers', 
            name='Positive Mentions',
            line=dict(color='green')
        ))
        fig_trend.add_trace(go.Scatter(
            x=trend_data['Month'], 
            y=trend_data['Negative Mentions'], 
            mode='lines+markers', 
            name='Negative Mentions',
            line=dict(color='red')
        ))
        fig_trend.update_layout(title='Monthly News Sentiment Trend')
        st.plotly_chart(fig_trend)

        # Keyword Frequency
        st.subheader('Most Discussed Keywords')
        keywords = self.news_analysis['keyword_frequency']
        fig_keywords = px.bar(
            x=list(keywords.keys()), 
            y=list(keywords.values()), 
            title='Keyword Frequency in News Coverage'
        )
        st.plotly_chart(fig_keywords)

        # Key News Stories
        st.subheader('Top News Stories')
        for story in self.news_analysis['key_news_stories']:
            st.markdown(f"""
            ### {story['Title']}
            - **Source**: {story['Source']}
            - **Date**: {story['Date']}
            - **Sentiment**: {story['Sentiment']}
            - **Summary**: {story['Summary']}
            - **Potential Impact**: {story['Impact']}
            ---
            """)

        # News Sources
        st.subheader('News Sources Analyzed')
        st.write("Sources: " + ", ".join(self.news_analysis['news_sources']))


def main():
    dashboard = ZomatoDashboard()
    dashboard.render_dashboard()

if __name__ == "__main__":
    main()
