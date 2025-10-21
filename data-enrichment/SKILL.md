---
name: enriching-tables-with-web-data
description: Enriches Excel tables with up-to-date web data using Bright Data MCP tools. Use when the user asks to enrich, update, or add information to spreadsheet data from LinkedIn, Instagram, Amazon, e-commerce sites, social media, or any web source. Supports company profiles, product data, social media metrics, reviews, and more.
---

# Table Enrichment with Bright Data

Enrich Excel tables with current web data using Bright Data's 60+ MCP tools.

## Requirements

Install openpyxl for Excel file handling:

```bash
pip install openpyxl --break-system-packages
```

## Workflow

### 1. Analyze the table

Read the Excel file and identify:
- Columns that contain identifiers (URLs, usernames, product IDs, company names)
- Columns that need enrichment (empty or to be updated)
- Data type (social media, e-commerce, business, etc.)

```python
import openpyxl

workbook = openpyxl.load_workbook("file.xlsx")
sheet = workbook.active

# Read headers and first few rows to understand structure
headers = [cell.value for cell in sheet[1]]
sample_data = [[cell.value for cell in row] for row in list(sheet.rows)[1:6]]
```

### 2. Match tools to data type

Based on identifiers in the table, select appropriate Bright Data tools:

**Social Media:**
- `BrightData:web_data_linkedin_person_profile` - LinkedIn profiles
- `BrightData:web_data_linkedin_company_profile` - LinkedIn companies
- `BrightData:web_data_instagram_profiles` - Instagram profiles
- `BrightData:web_data_tiktok_profiles` - TikTok profiles
- `BrightData:web_data_youtube_profiles` - YouTube channels

**E-commerce:**
- `BrightData:web_data_amazon_product` - Amazon products
- `BrightData:web_data_walmart_product` - Walmart products
- `BrightData:web_data_ebay_product` - eBay products
- `BrightData:web_data_etsy_products` - Etsy products

**Business:**
- `BrightData:web_data_crunchbase_company` - Company data
- `BrightData:web_data_zoominfo_company_profile` - ZoomInfo data

**General:**
- `BrightData:scrape_as_markdown` - Any public webpage

### 3. Enrich data row by row

For each row, call the appropriate MCP tool and extract relevant fields:

```python
# Example: Enriching LinkedIn profiles
for row_idx, row in enumerate(sheet.iter_rows(min_row=2), start=2):
    linkedin_url = row[url_column_idx].value
    
    if linkedin_url:
        # Call BrightData:web_data_linkedin_person_profile
        # Extract: name, title, company, location, connections, etc.
        # Write to corresponding columns
        
        sheet.cell(row=row_idx, column=name_col).value = profile_data['name']
        sheet.cell(row=row_idx, column=title_col).value = profile_data['title']
```

### 4. Handle errors and missing data

- Skip rows with invalid/missing identifiers
- Log which rows were enriched successfully
- Note rate limits or tool failures
- Preserve original data

### 5. Save enriched file

Save to `/mnt/user-data/outputs/`:

```python
output_path = '/mnt/user-data/outputs/enriched_table.xlsx'
workbook.save(output_path)
```

Provide link: `[View enriched table](computer:///mnt/user-data/outputs/enriched_table.xlsx)`

## Tool selection logic

**If table has LinkedIn URLs** → Use `BrightData:web_data_linkedin_person_profile` or `BrightData:web_data_linkedin_company_profile`

**If table has Instagram URLs** → Use `BrightData:web_data_instagram_profiles`

**If table has Amazon URLs (with /dp/)** → Use `BrightData:web_data_amazon_product`

**If table has product names but no URLs** → Use `BrightData:search_engine` to find URLs first, then scrape

**If table has company names** → Search for LinkedIn/Crunchbase URLs, then enrich

**If URLs are present but platform unknown** → Use `BrightData:scrape_as_markdown`

## Best practices

- **Batch similar requests**: Group rows by data type before calling tools
- **Start small**: Test enrichment on first 3-5 rows before processing entire table
- **Preserve originals**: Create new columns for enriched data
- **Show progress**: Update user after every 10-20 rows processed
- **Handle nulls**: Explicitly mark cells where data couldn't be retrieved

## Example enrichment types

**LinkedIn profiles → Add:** job title, company, location, connections, industry

**Instagram accounts → Add:** followers, posts count, engagement rate, bio

**Amazon products → Add:** price, rating, review count, availability, seller

**Company names → Add:** LinkedIn URL, website, employee count, funding, industry

**Generic URLs → Add:** page title, description, key content, last updated
