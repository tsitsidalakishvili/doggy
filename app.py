import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

# Set the page configuration
st.set_page_config(page_title="Dog Shelter Project Proposal", layout="wide")

# Title
st.title("Interactive Project Proposal for Establishing a Dog Shelter in Georgia")

# Navigation Sidebar
st.sidebar.title("Navigation")
sections = [
    "Introduction",
    "Problem Statement",
    "Project Objectives",
    "Project Description",
    "Implementation Plan",
    "Budget",
    "Sustainability Plan",
    "Monitoring and Evaluation",
    "Risk Management",
    "Appendices",
]
selection = st.sidebar.radio("Go to", sections)

# Introduction with Interactive Budget and Donation Features
if selection == "Introduction":
    st.header("1. Executive Summary")
    
    # Executive Summary Text
    st.markdown("""
    **Introduction:**
    Georgia is currently grappling with a significant stray dog population, leading to public health concerns, environmental issues, and animal welfare challenges. The absence of dedicated shelters exacerbates these problems, as stray dogs often face harsh living conditions without access to necessary care.
    
    **Objectives:**
    - **Primary Goal:** Establish a state-of-the-art dog shelter in Tbilisi, Georgia.
    - **Secondary Goals:**
      - Reduce the stray dog population by 30% within three years.
      - Promote a culture of adoption and responsible pet ownership.
      - Enhance public health and safety by managing stray dog-related incidents.
      - Educate the community on animal welfare and humane treatment of stray dogs.
    
    **Funding Request:**
    We are seeking a grant of **$250,000** to cover the costs of construction, equipment, staffing, and initial operations of the dog shelter.
    
    **Impact:**
    The establishment of this shelter will provide a safe haven for stray dogs, offer veterinary care, facilitate adoptions, and significantly improve the quality of life for both animals and the community. It will also foster a compassionate culture towards animal welfare in Georgia.
    """)
    
    st.markdown("---")
    
    # Interactive Budget Allocation and Donation Impact
    st.subheader("Interactive Budget Allocation and Donation Impact")
    
    # Define budget categories
    budget_categories = ['Construction', 'Equipment', 'Staffing', 'Operations', 'Programs', 'Contingency']
    default_budget = {
        'Construction': 60000,
        'Equipment': 25000,
        'Staffing': 80000,
        'Operations': 22500,
        'Programs': 17500,
        'Contingency': 10000
    }
    
    # Sidebar inputs for budget allocation
    st.sidebar.header("Adjust Budget Allocation")
    budget_allocation = {}
    total_budget = 250000
    
    # Sliders for each budget category except 'Contingency'
    allocated = 0
    for category in budget_categories[:-1]:
        max_alloc = total_budget - allocated - 5000  # Reserve at least $5,000 for 'Contingency'
        allocation = st.sidebar.slider(
            f"Allocate to {category}",
            min_value=0,
            max_value=total_budget,
            value=default_budget[category],
            step=1000
        )
        budget_allocation[category] = allocation
        allocated += allocation
    
    # 'Contingency' gets the remaining budget
    budget_allocation['Contingency'] = total_budget - allocated
    
    # Convert to DataFrame for display
    budget_df = pd.DataFrame({
        'Category': list(budget_allocation.keys()),
        'Amount (USD)': list(budget_allocation.values())
    })
    
    # Display Budget Table
    st.table(budget_df)
    
    # Plot Budget Allocation Pie Chart
    st.subheader("Budget Allocation")
    fig_budget = px.pie(
        budget_df,
        values='Amount (USD)',
        names='Category',
        title='Budget Allocation',
        hole=0.4
    )
    st.plotly_chart(fig_budget, use_container_width=True)
    
    # Cost Analysis
    st.subheader("Cost Analysis")
    
    # Define total number of stray dogs
    total_stray_dogs = 15000
    
    # Calculate cost to save one dog
    cost_per_dog = total_budget / total_stray_dogs
    
    st.metric(
        label="Cost to Save One Stray Dog",
        value=f"${cost_per_dog:,.2f}"
    )
    
    # Donation Impact
    st.subheader("Donation Impact")
    
    # Input for additional donations
    additional_donation = st.number_input(
        "Enter additional donation amount (USD):",
        min_value=0,
        step=1000,
        value=0
    )
    
    # Calculate new total budget
    new_total_budget = total_budget + additional_donation
    
    # Calculate number of dogs that can be saved with new budget
    dogs_saved = new_total_budget / cost_per_dog
    
    # Display results
    st.metric(
        label="Number of Stray Dogs Saved with Additional Donation",
        value=f"{int(dogs_saved):,} dogs"
    )
    
    # Visualization of Donation Impact
    st.subheader("Donation Impact Visualization")
    
    # Create DataFrame for visualization
    donation_data = pd.DataFrame({
        'Total Budget (USD)': [total_budget, new_total_budget],
        'Dogs Saved': [total_budget / cost_per_dog, dogs_saved]
    }, index=['Current Budget', 'After Donation'])
    
    # Bar Chart
    fig_donation = px.bar(
        donation_data,
        x=donation_data.index,
        y='Dogs Saved',
        title='Impact of Additional Donations on Dogs Saved',
        labels={'index': 'Budget Scenario', 'Dogs Saved': 'Number of Dogs Saved'},
        text='Dogs Saved'
    )
    fig_donation.update_traces(texttemplate='%{text:.0f}', textposition='auto')
    st.plotly_chart(fig_donation, use_container_width=True)
    
    # Summary Metrics
    st.subheader("Summary")
    
    st.markdown(f"""
    - **Current Total Budget:** ${total_budget:,.2f}
    - **Cost to Save One Stray Dog:** ${cost_per_dog:,.2f}
    - **Additional Donation:** ${additional_donation:,.2f}
    - **New Total Budget:** ${new_total_budget:,.2f}
    - **Total Number of Dogs Saved:** {int(dogs_saved):,} dogs
    """)
    
    # Optional: Interactive Sliders for More Granularity
    st.subheader("Interactive Donation Slider")
    
    donation_slider = st.slider(
        "Select additional donation amount (USD):",
        min_value=0,
        max_value=100000,
        step=1000,
        value=additional_donation
    )
    
    # Recalculate with slider
    new_total_budget_slider = total_budget + donation_slider
    dogs_saved_slider = new_total_budget_slider / cost_per_dog
    
    st.metric(
        label="Number of Stray Dogs Saved with Selected Donation",
        value=f"{int(dogs_saved_slider):,} dogs"
    )
    
    # Update Visualization
    donation_data_slider = pd.DataFrame({
        'Total Budget (USD)': [total_budget, new_total_budget_slider],
        'Dogs Saved': [total_budget / cost_per_dog, dogs_saved_slider]
    }, index=['Current Budget', 'After Donation'])
    
    fig_donation_slider = px.bar(
        donation_data_slider,
        x=donation_data_slider.index,
        y='Dogs Saved',
        title='Impact of Selected Donation on Dogs Saved',
        labels={'index': 'Budget Scenario', 'Dogs Saved': 'Number of Dogs Saved'},
        text='Dogs Saved'
    )
    fig_donation_slider.update_traces(texttemplate='%{text:.0f}', textposition='auto')
    st.plotly_chart(fig_donation_slider, use_container_width=True)

# Problem Statement
elif selection == "Problem Statement":
    st.header("2. Problem Statement")
    st.markdown("""
    **Current Situation:**
    Georgia has an estimated stray dog population of **15,000** in major cities, including Tbilisi, Batumi, Kutaisi, and Rustavi. The number of stray dogs has been increasing by **5% annually** over the past five years, with Tbilisi alone accounting for approximately **60%** of the total stray population.

    **Challenges:**
    - **Lack of Shelters:** No dedicated facilities exist to house and care for stray dogs, resulting in dogs living in unsanitary and unsafe conditions.
    - **Inadequate Animal Control:** Limited resources for managing and controlling stray dog populations, leading to unchecked breeding and increased numbers.
    - **Public Health Risks:** Stray dogs contribute to the spread of diseases such as rabies and pose risks of bites and traffic accidents.
    - **Absence of Adoption Culture:** Limited awareness and infrastructure to support the adoption of stray dogs, leading to prolonged shelter times and decreased adoption rates.

    **Impact:**
    Stray dogs negatively affect communities by:
    - **Safety Concerns:** Increased incidents of dog bites and aggressive behavior towards humans.
    - **Disease Transmission:** Higher risk of rabies and other zoonotic diseases spreading within the population.
    - **Environmental Degradation:** Stray dogs contribute to noise pollution, waste accumulation, and disturbances in public spaces.
    - **Negative Perceptions:** Public perception of poor animal welfare standards, affecting community morale and international reputation.
    """)

# Project Objectives
elif selection == "Project Objectives":
    st.header("3. Project Objectives")
    st.markdown("""
    **Primary Goals:**
    1. **Establish a Fully Equipped Dog Shelter:**
       - Location: Tbilisi, Georgia.
       - Capacity: 200 dogs.

    2. **Provide Comprehensive Care:**
       - Veterinary services, including vaccinations, treatments, and surgeries.
       - Regular grooming and hygiene maintenance.
       - Behavioral training and rehabilitation programs.

    3. **Promote Adoption and Responsible Pet Ownership:**
       - Facilitate the adoption process through an organized adoption center.
       - Conduct community outreach and education programs.

    4. **Educate the Community:**
       - Raise awareness about animal welfare and the benefits of adopting stray dogs.
       - Implement spay/neuter campaigns to control stray populations.

    **Specific Objectives:**
    - **Population Reduction:** Decrease the stray dog population by **30%** within three years through rescue, sterilization, and adoption initiatives.
    - **Adoption Rates:** Achieve an annual adoption rate of **500 dogs**.
    - **Community Engagement:** Conduct **monthly** educational workshops and **quarterly** outreach events to engage the community.
    - **Sustainability:** Develop revenue streams and partnerships to ensure the shelter's financial sustainability beyond initial funding.
    """)

# Project Description
elif selection == "Project Description":
    st.header("4. Project Description")
    st.subheader("4.1 Shelter Facilities")
    st.markdown("""
    **Location:**
    The proposed shelter will be situated in Tbilisi, the capital city of Georgia, chosen for its high stray dog population and accessibility. The selected area is a spacious plot of **5,000 square meters** in the outskirts of the city, providing ample space for facilities and outdoor areas for dogs to exercise.

    **Structure:**
    - **Kennels:**
      - **Quantity:** 200 individual kennels.
      - **Specifications:** Each kennel measures **2m x 2m**, with proper ventilation, natural lighting, and secure fencing to ensure safety and comfort.
      
    - **Veterinary Clinic:**
      - **Facilities:** Two examination rooms, one surgical suite, and an isolation ward for sick or newly arrived dogs.
      - **Equipment:** Diagnostic tools including X-ray machines, surgical instruments, and laboratory equipment.
    
    - **Grooming Area:**
      - **Stations:** Five grooming stations equipped with baths, dryers, grooming tables, and necessary supplies.
      
    - **Administrative Offices:**
      - **Space:** Office space for staff, management, and administrative operations, including meeting rooms and storage.
      
    - **Adoption Center:**
      - **Design:** A welcoming area where potential adopters can interact with dogs, featuring comfortable seating, informational displays, and adoption application stations.
      
    - **Quarantine Area:**
      - **Purpose:** To isolate and monitor new or sick animals, preventing the spread of diseases within the shelter.
    """)
    
    st.subheader("4.2 Equipment and Supplies")
    st.markdown("""
    **Veterinary Equipment:**
    - **Examination Tables:** 4 units.
    - **Surgical Instruments Set:** 2 complete sets.
    - **X-ray Machine:** 1 unit.
    - **Diagnostic Tools:** Blood analyzers, thermometers, and sterilization equipment.
    
    **Grooming Supplies:**
    - **Grooming Tables:** 5 units.
    - **Clippers and Trimmers:** 10 sets.
    - **Bathing Equipment:** 5 baths with water heaters.
    - **Dryers:** 5 high-velocity dryers.
    
    **Kennel Supplies:**
    - **Dog Beds:** 200 beds, washable and durable.
    - **Fencing Panels:** 200 units for secure enclosures.
    - **Feeding Bowls:** 200 stainless steel bowls.
    - **Cleaning Equipment:** Power washers, disinfectants, and waste disposal systems.
    
    **Administrative Tools:**
    - **Computers:** 10 units for staff.
    - **Office Furniture:** 15 sets of desks and chairs.
    - **Software:** Animal tracking and management software.
    
    **Safety and Sanitation:**
    - **Disinfectant Solutions:** 50 liters.
    - **Protective Gear:** 100 pairs of gloves, masks, and aprons for staff.
    - **Waste Disposal Systems:** Secure bins and biohazard containers.
    
    **Equipment List:**
    
    | **Category**          | **Items**                        | **Quantity** |
    |-----------------------|----------------------------------|--------------|
    | **Veterinary**        | Examination Tables               | 4            |
    |                       | Surgical Instruments Set         | 2 sets       |
    |                       | X-ray Machine                    | 1            |
    |                       | Diagnostic Tools                 | Various      |
    | **Grooming**          | Grooming Tables                  | 5            |
    |                       | Clippers and Trimmers            | 10 sets      |
    |                       | Bathing Equipment                | 5 baths      |
    |                       | Dryers                           | 5 units      |
    | **Kennel**            | Dog Beds                         | 200          |
    |                       | Fencing Panels                   | 200 units    |
    |                       | Feeding Bowls                    | 200          |
    |                       | Cleaning Equipment               | Various      |
    | **Administrative**    | Computers                        | 10           |
    |                       | Office Furniture                 | 15 sets      |
    |                       | Software                         | 5 licenses   |
    | **Safety & Sanitation**| Disinfectant Solutions           | 50 liters    |
    |                       | Protective Gear                  | 100 pairs    |
    |                       | Waste Disposal Systems           | Various      |
    """)
    
    st.subheader("4.3 Services Provided")
    st.markdown("""
    **Rescue and Intake:**
    - **Process:** Collaborate with local authorities and community members to rescue stray dogs. Implement a structured intake process to assess and categorize each dog upon arrival.
      
    **Medical Care:**
    - **Routine Check-ups:** Regular health assessments, vaccinations, and parasite control.
    - **Emergency Care:** Immediate treatment for injured or ill dogs.
    - **Surgical Procedures:** Spaying/neutering and other necessary surgeries.
    
    **Grooming and Hygiene:**
    - **Regular Grooming:** Bathing, brushing, and nail trimming to maintain health and appearance.
    - **Hygiene Maintenance:** Ensuring cleanliness of kennels and common areas to prevent disease spread.
    
    **Behavioral Training:**
    - **Rehabilitation Programs:** Socialization and training to improve adoptability.
    - **Behavioral Assessments:** Evaluating each dog's temperament and needs.
    
    **Adoption Services:**
    - **Adoption Process:** Screening potential adopters, conducting home visits, and providing adoption counseling.
    - **Post-Adoption Support:** Follow-up to ensure successful integration of dogs into new homes.
    
    **Community Outreach:**
    - **Educational Programs:** Workshops and seminars on responsible pet ownership and animal welfare.
    - **Spay/Neuter Campaigns:** Initiatives to control the stray population through sterilization.
    """)

# Implementation Plan
elif selection == "Implementation Plan":
    st.header("5. Implementation Plan")
    st.markdown("""
    **Phase 1: Planning and Site Acquisition (Months 1-3)**
    - **Secure Location:** Finalize the purchase or lease of the 5,000 sqm plot in Tbilisi.
    - **Obtain Permits:** Acquire necessary construction and operational permits from local authorities.
    - **Design Finalization:** Work with architects to finalize shelter design and layout.
    
    **Phase 2: Construction and Setup (Months 4-8)**
    - **Construction:** Build the shelter infrastructure, including kennels, clinic, grooming area, and administrative offices.
    - **Equipment Installation:** Set up veterinary equipment, grooming stations, administrative tools, and safety systems.
    
    **Phase 3: Staffing and Training (Months 9-10)**
    - **Hire Staff:** Recruit veterinarians, groomers, caretakers, administrative personnel, and volunteers.
    - **Training Programs:** Conduct comprehensive training on shelter operations, animal care, and safety protocols.
    
    **Phase 4: Launch Operations (Month 11)**
    - **Begin Operations:** Start rescue and intake processes.
    - **Community Outreach:** Initiate educational programs and adoption campaigns.
    - **Adoption Events:** Host the first adoption fair to connect dogs with potential adopters.
    
    **Phase 5: Monitoring and Evaluation (Ongoing from Month 12)**
    - **Track KPIs:** Monitor key performance indicators such as number of dogs rescued, treated, and adopted.
    - **Adjust Programs:** Modify and improve programs based on feedback and outcomes.
    - **Annual Reviews:** Conduct comprehensive evaluations to assess progress and plan for future growth.
    """)
    
    st.subheader("Project Timeline")

    # Updated Gantt Data with 'Ongoing' replaced
    gantt_data = pd.DataFrame({
        'Task': [
            'Planning & Site Acquisition',
            'Construction & Setup',
            'Staffing & Training',
            'Launch Operations',
            'Monitoring & Evaluation'
        ],
        'Start': [
            '2025-02-01',
            '2025-05-01',
            '2025-10-01',
            '2026-01-01',
            '2026-02-01'
        ],
        'Finish': [
            '2025-04-30',
            '2025-08-31',
            '2025-10-31',
            '2026-01-31',
            '2026-12-31'  # Replaced 'Ongoing' with a specific date
        ]
    })

    # Convert to datetime
    gantt_data['Start'] = pd.to_datetime(gantt_data['Start'])
    gantt_data['Finish'] = pd.to_datetime(gantt_data['Finish'])

    # Display DataFrame (optional)
    st.write(gantt_data)

    # Create and display Gantt Chart
    fig = px.timeline(
        gantt_data,
        x_start="Start",
        x_end="Finish",
        y="Task",
        title="Project Timeline",
        labels={"Start": "Start Date", "Finish": "End Date", "Task": "Phase"}
    )
    fig.update_yaxes(categoryorder="total ascending")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# Budget
elif selection == "Budget":
    st.header("6. Budget")
    st.markdown("""
    **Total Funding Requested:** **$250,000**

    **Detailed Budget Breakdown:**
    """)
    # (The Budget section can remain as previously implemented or be adjusted as needed.)
    # ...

# Sustainability Plan with Interactive Budget Elements
elif selection == "Sustainability Plan":
    st.header("7. Sustainability Plan")
    
    st.markdown("""
    Ensuring the long-term sustainability of the dog shelter is crucial for its ongoing operations and impact. This section outlines the revenue streams and strategies that will maintain and grow the shelter's financial health.
    """)
    
    # Interactive Revenue Streams
    st.subheader("Interactive Revenue Streams")
    
    # Define revenue categories
    revenue_categories = ['Adoption Fees', 'Merchandise Sales', 'Veterinary Services', 'Grooming Services', 'Training Programs', 'Other']
    default_revenue = {
        'Adoption Fees': 20,          # in Euros per adoption
        'Merchandise Sales': 10,      # average price per item
        'Veterinary Services': 50,    # average fee per service
        'Grooming Services': 30,      # average fee per grooming session
        'Training Programs': 100,     # average fee per training session
        'Other': 0                    # placeholder for additional revenue streams
    }
    
    # Sidebar inputs for revenue streams
    st.sidebar.header("Adjust Revenue Streams")
    revenue_input = {}
    
    for category in revenue_categories:
        if category == 'Adoption Fees':
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Euros per adoption)",
                min_value=0,
                step=1,
                value=default_revenue[category]
            )
        elif category == 'Merchandise Sales':
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Average price per item in Euros)",
                min_value=0,
                step=1,
                value=default_revenue[category]
            )
        elif category == 'Veterinary Services':
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Average fee per service in Euros)",
                min_value=0,
                step=5,
                value=default_revenue[category]
            )
        elif category == 'Grooming Services':
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Average fee per session in Euros)",
                min_value=0,
                step=5,
                value=default_revenue[category]
            )
        elif category == 'Training Programs':
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Average fee per session in Euros)",
                min_value=0,
                step=10,
                value=default_revenue[category]
            )
        else:
            revenue_input[category] = st.sidebar.number_input(
                f"Set {category} (Euros)",
                min_value=0,
                step=10,
                value=default_revenue[category]
            )
    
    st.markdown("---")
    
    # Input for expected monthly units
    st.subheader("Expected Monthly Units")
    
    # Define expected units for each revenue stream
    expected_units = {}
    expected_units['Adoption Fees'] = st.number_input(
        "Expected number of adoptions per month:",
        min_value=0,
        step=1,
        value=50
    )
    expected_units['Merchandise Sales'] = st.number_input(
        "Expected number of merchandise items sold per month:",
        min_value=0,
        step=1,
        value=100
    )
    expected_units['Veterinary Services'] = st.number_input(
        "Expected number of veterinary services per month:",
        min_value=0,
        step=1,
        value=20
    )
    expected_units['Grooming Services'] = st.number_input(
        "Expected number of grooming sessions per month:",
        min_value=0,
        step=1,
        value=30
    )
    expected_units['Training Programs'] = st.number_input(
        "Expected number of training sessions per month:",
        min_value=0,
        step=1,
        value=10
    )
    expected_units['Other'] = st.number_input(
        "Expected revenue from other sources per month (Euros):",
        min_value=0,
        step=10,
        value=0
    )
    
    # Calculate monthly revenue for each stream
    monthly_revenue = {}
    for category in revenue_categories:
        if category == 'Other':
            monthly_revenue[category] = expected_units[category]
        else:
            monthly_revenue[category] = revenue_input[category] * expected_units[category]
    
    # Convert to DataFrame
    revenue_df = pd.DataFrame({
        'Revenue Stream': list(monthly_revenue.keys()),
        'Monthly Revenue (Euros)': list(monthly_revenue.values())
    })
    
    # Display Revenue Table
    st.table(revenue_df)
    
    # Calculate Total Monthly and Annual Revenue
    total_monthly_revenue = sum(monthly_revenue.values())
    total_annual_revenue = total_monthly_revenue * 12
    
    st.subheader("Total Revenue")
    st.metric(
        label="Total Monthly Revenue",
        value=f"€{total_monthly_revenue:,.2f}"
    )
    st.metric(
        label="Total Annual Revenue",
        value=f"€{total_annual_revenue:,.2f}"
    )
    
    st.markdown("---")
    
    # Allocation of Funds
    st.subheader("Allocation of Revenue")
    
    # Define allocation categories (these should align with your budget or operational needs)
    allocation_categories = ['Dog Care', 'Facility Maintenance', 'Staff Salaries', 'Operational Costs', 'Emergency Fund', 'Other']
    
    # Default allocation percentages
    default_allocation = {
        'Dog Care': 50,            # 50%
        'Facility Maintenance': 15, # 15%
        'Staff Salaries': 20,      # 20%
        'Operational Costs': 10,   # 10%
        'Emergency Fund': 3,       # 3%
        'Other': 2                 # 2%
    }
    
    # Sidebar inputs for allocation
    st.sidebar.header("Adjust Allocation Percentages")
    allocation_percentages = {}
    allocated_percent = 0
    for category in allocation_categories[:-1]:
        max_percent = 100 - allocated_percent - 1  # Reserve at least 1% for 'Other'
        percent = st.sidebar.slider(
            f"Allocate to {category} (%)",
            min_value=0,
            max_value=100,
            value=default_allocation[category],
            step=1
        )
        allocation_percentages[category] = percent
        allocated_percent += percent
    
    # 'Other' gets the remaining percentage
    allocation_percentages['Other'] = 100 - allocated_percent
    
    # Convert to DataFrame
    allocation_df = pd.DataFrame({
        'Category': list(allocation_percentages.keys()),
        'Percentage (%)': list(allocation_percentages.values())
    })
    
    # Display Allocation Table
    st.table(allocation_df)
    
    # Calculate allocated funds
    allocated_funds = {}
    for category in allocation_categories:
        allocated_funds[category] = (allocation_percentages[category] / 100) * total_annual_revenue
    
    # Convert to DataFrame
    allocated_funds_df = pd.DataFrame({
        'Allocation Category': list(allocated_funds.keys()),
        'Annual Allocation (Euros)': list(allocated_funds.values())
    })
    
    # Display Allocation Table
    st.table(allocated_funds_df)
    
    # Plot Allocation Pie Chart
    st.subheader("Revenue Allocation")
    fig_allocation = px.pie(
        allocated_funds_df,
        values='Annual Allocation (Euros)',
        names='Allocation Category',
        title='Annual Revenue Allocation',
        hole=0.4
    )
    st.plotly_chart(fig_allocation, use_container_width=True)
    
    # Summary Metrics
    st.subheader("Summary of Revenue and Allocation")
    
    st.markdown(f"""
    - **Total Monthly Revenue:** €{total_monthly_revenue:,.2f}
    - **Total Annual Revenue:** €{total_annual_revenue:,.2f}
    - **Dog Care Allocation:** €{allocated_funds['Dog Care']:,.2f} ({allocation_percentages['Dog Care']}%)
    - **Facility Maintenance Allocation:** €{allocated_funds['Facility Maintenance']:,.2f} ({allocation_percentages['Facility Maintenance']}%)
    - **Staff Salaries Allocation:** €{allocated_funds['Staff Salaries']:,.2f} ({allocation_percentages['Staff Salaries']}%)
    - **Operational Costs Allocation:** €{allocated_funds['Operational Costs']:,.2f} ({allocation_percentages['Operational Costs']}%)
    - **Emergency Fund Allocation:** €{allocated_funds['Emergency Fund']:,.2f} ({allocation_percentages['Emergency Fund']}%)
    - **Other Allocation:** €{allocated_funds['Other']:,.2f} ({allocation_percentages['Other']}%)
    """)

# The rest of the sections remain unchanged
elif selection == "Monitoring and Evaluation":
    st.header("8. Monitoring and Evaluation")
    st.markdown("""
    **Key Performance Indicators (KPIs):**
    - **Rescue Operations:** Number of stray dogs rescued and admitted to the shelter monthly.
    - **Medical Care:** Number of veterinary treatments, surgeries, and vaccinations performed.
    - **Adoption Rates:** Number of dogs adopted annually.
    - **Community Engagement:** Attendance at educational workshops and participation in outreach events.
    - **Financial Metrics:** Fundraising targets, donation amounts, and revenue from services.
    
    **Evaluation Methods:**
    - **Data Collection:** Maintain detailed records of all rescue operations, medical treatments, adoptions, and financial transactions.
    - **Feedback Mechanisms:** Collect feedback from adopters, community members, and staff to assess satisfaction and areas for improvement.
    - **Regular Reporting:** Produce quarterly and annual reports to review progress against objectives and KPIs.
    - **Third-Party Audits:** Conduct independent audits to ensure transparency and accountability.
    
    **Continuous Improvement:**
    - **Program Adjustments:** Modify programs based on evaluation findings to enhance effectiveness and impact.
    - **Staff Training:** Provide ongoing training to staff and volunteers to improve skills and service quality.
    """)

elif selection == "Risk Management":
    st.header("9. Risk Management")
    st.markdown("""
    **Potential Risks:**
    1. **Insufficient Funding:**
       - **Impact:** May hinder construction, staffing, and operations.
       - **Mitigation:** Diversify funding sources, apply for multiple grants, and launch fundraising campaigns.
    
    2. **High Operational Costs:**
       - **Impact:** Could strain the shelter's financial sustainability.
       - **Mitigation:** Implement cost-saving measures, seek in-kind donations, and optimize resource allocation.
    
    3. **Public Resistance:**
       - **Impact:** Lack of community support may affect adoption rates and fundraising efforts.
       - **Mitigation:** Conduct awareness campaigns, engage community leaders, and demonstrate the shelter's benefits.
    
    4. **Disease Outbreaks:**
       - **Impact:** Could compromise animal health and shelter operations.
       - **Mitigation:** Maintain strict hygiene protocols, quarantine new arrivals, and provide regular veterinary care.
    
    5. **Regulatory Compliance Issues:**
       - **Impact:** Non-compliance could lead to legal challenges or closure.
       - **Mitigation:** Stay informed about local regulations, seek legal counsel, and ensure all operations adhere to laws.
    
    **Contingency Plans:**
    - **Emergency Funds:** Allocate a portion of the budget for emergencies.
    - **Backup Suppliers:** Establish relationships with multiple suppliers to prevent shortages.
    - **Crisis Management Team:** Form a team responsible for handling emergencies and unexpected challenges.
    """)

elif selection == "Appendices":
    st.header("10. Appendices")
    
    st.subheader("A. Organizational Structure")
    st.markdown("""
    **Shelter Management:**
    
    | **Position**          | **Responsibilities**                                    |
    |-----------------------|---------------------------------------------------------|
    | **Shelter Director**  | Oversees all operations, strategic planning, and leadership. |
    | **Veterinary Manager**| Manages medical care, oversees veterinary staff, and ensures animal health. |
    | **Grooming Manager**  | Supervises grooming services and maintains hygiene standards. |
    | **Operations Manager**| Handles daily operations, logistics, and facility maintenance. |
    | **Administrative Staff**| Manages administrative tasks, financial records, and donor relations. |
    | **Caretakers/Volunteers**| Provide daily care, feeding, and exercise for the dogs. |
    """)

    st.subheader("Organizational Chart")
    st.image("https://via.placeholder.com/600x400.png?text=Organizational+Chart", caption="Organizational Structure Diagram")

    st.subheader("B. Letters of Support")
    st.markdown("""
    *Note: Include sample letters from local authorities, community leaders, and partner organizations endorsing the project.*
    """)

    st.subheader("C. Detailed Budget Breakdown")
    st.markdown("""
    *Note: Provide an expanded version of the budget table with specific cost items and justifications.*
    """)

    st.subheader("D. Project Timeline")
    st.markdown("""
    *Note: Insert a detailed Gantt chart showing project phases, tasks, and deadlines over a 12-month period.*
    """)

    st.subheader("E. Case Studies")
    st.markdown("""
    **Example 1: Successful Dog Shelter in Neighboring Country**
    - **Location:** Armenia.
    - **Achievements:** Reduced stray dog population by 25% in two years, achieved a high adoption rate through community programs.
    - **Lessons Learned:** Importance of community engagement and robust veterinary services.
    
    **Example 2: Community-Driven Shelter in Eastern Europe**
    - **Location:** Romania.
    - **Achievements:** Established a self-sustaining shelter through volunteer programs and local partnerships.
    - **Lessons Learned:** Leveraging local resources and fostering volunteer involvement enhances sustainability.
    """)

# Sample Visuals and Templates
elif selection == "Sample Visuals and Templates":
    st.header("Sample Visuals and Templates")
    
    st.subheader("A. Stray Dog Population Chart")
    st.image("https://via.placeholder.com/600x400.png?text=Stray+Dog+Population+Chart", caption="Stray Dog Population in Major Georgian Cities (2020-2024)")
    
    st.subheader("B. Budget Allocation Pie Chart")
    st.image("https://via.placeholder.com/600x400.png?text=Budget+Allocation+Pie+Chart", caption="Proposed Budget Allocation")
    
    st.subheader("C. Project Timeline Gantt Chart")
    st.image("https://via.placeholder.com/800x400.png?text=Project+Timeline+Gantt+Chart", caption="Project Timeline Gantt Chart")
    
    st.markdown("""
    ### **Export Proposal**
    To export this proposal, use your browser's print functionality and select "Save as PDF."
    """)

# Default Section
else:
    st.write("Select a section from the sidebar to view the project proposal.")
