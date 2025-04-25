import os
import sys
import importlib
import pathlib
import subprocess
import json
from datetime import datetime

# Terminal colors for better UI
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Order of scripts to run
EXAMPLES_DIR = "examples"
SCRIPTS_TO_RUN = [
    "auth.py",
    "get_balance.py",
    "get_bins.py"
]

def main():
    """Run the tests in a specific order with simplified output"""
    print(f"{Colors.BOLD}API-CARD PYTHON SDK - BASIC TEST{Colors.ENDC}\n")
    
    # Check if required scripts exist
    for script in SCRIPTS_TO_RUN:
        script_path = os.path.join(EXAMPLES_DIR, script)
        if not os.path.exists(script_path):
            print(f"{Colors.RED}Missing required script: {script}{Colors.ENDC}")
            return
    
    # Run scripts in order
    start_time = datetime.now()
    
    # 1. Authentication
    print(f"{Colors.BOLD}1. Testing Authentication...{Colors.ENDC}")
    auth_result = run_script("auth.py")
    if not auth_result.get('Good', False):
        print(f"{Colors.RED}Authentication failed: {auth_result.get('Message', 'Unknown error')}{Colors.ENDC}")
        return
    print(f"{Colors.GREEN}✓ Authentication successful!{Colors.ENDC}\n")
    
    # 2. Get Balance
    print(f"{Colors.BOLD}2. Getting Account Balance...{Colors.ENDC}")
    balance_result = run_script("get_balance.py")
    if balance_result.get('Good', False) and 'Result' in balance_result:
        result = balance_result.get('Result', {})
        print(f"{Colors.GREEN}✓ Success!{Colors.ENDC}")
        print(f"   {Colors.CYAN}Balance USD: ${result.get('balance_usd', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Total Replenishment USD: ${result.get('total_replenishment_usd', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Total Spend USD: ${result.get('total_spend_usd', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Balance Cards: {result.get('balance_cards', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Total Cards: {result.get('total_cards', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Active Cards: {result.get('active_cards', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Active Cards Available Balance USD: ${result.get('active_cards_available_balance_usd', 0)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Is New Cards Available: {result.get('is_new_cards_available', False)}{Colors.ENDC}")
        print(f"   {Colors.CYAN}Top Up Required Amount: ${result.get('top_up_required_amount', 0)}{Colors.ENDC}")
    else:
        print(f"{Colors.RED}Failed to get balance: {balance_result}{Colors.ENDC}")
    print()
    
    # 3. Get Bins
    print(f"{Colors.BOLD}3. Checking Available Bins...{Colors.ENDC}")
    bins_result = run_script("get_bins.py")
    if bins_result.get('Status', -1) == 0 or bins_result.get('Good', False):
        # Different APIs might return bins in different formats
        # Check all possible locations
        bins = []
        if 'Result' in bins_result:
            # Handle the case where Result is directly a list of bins
            if isinstance(bins_result['Result'], list):
                bins = bins_result['Result']
            # Handle the case where Result is a dict with a 'bins' key
            elif isinstance(bins_result['Result'], dict) and 'bins' in bins_result['Result']:
                bins = bins_result['Result'].get('bins', [])
        # Fallback to direct 'bins' key if present
        elif 'bins' in bins_result:
            bins = bins_result['bins']
        # Last resort - the result itself might be a list
        elif isinstance(bins_result, list):
            bins = bins_result
            
        if not bins:
            print(f"{Colors.YELLOW}No bins available. Please go to api-card.com to register and open a bin.{Colors.ENDC}")
        else:
            print(f"{Colors.GREEN}✓ Found {len(bins)} bin(s){Colors.ENDC}")
            # Filter to show only bins where the user has access
            accessible_bins = [b for b in bins if isinstance(b, dict) and b.get('has_access', False)]
            if accessible_bins:
                print(f"{Colors.GREEN}✓ You have access to {len(accessible_bins)} bin(s){Colors.ENDC}")
                
                # Show accessible bins first
                for i, bin_info in enumerate(accessible_bins[:3], 1):
                    bin_number = bin_info.get("bin_number", bin_info.get("bin", "N/A"))
                    network = bin_info.get("network", "")
                    bin_name = f"{network} {bin_number}"
                    print(f"   {Colors.GREEN}Bin {i}: {bin_name} (Accessible){Colors.ENDC}")
                
                if len(accessible_bins) > 3:
                    print(f"   {Colors.GREEN}... and {len(accessible_bins) - 3} more accessible bins{Colors.ENDC}")
            else:
                print(f"{Colors.YELLOW}You don't have access to any BINs yet.{Colors.ENDC}")
                print(f"{Colors.YELLOW}Please contact support to get access to one of your BINs.{Colors.ENDC}")
                
                # Show a few bins regardless of access
                for i, bin_info in enumerate(bins[:3], 1):
                    if isinstance(bin_info, dict):
                        bin_number = bin_info.get("bin_number", bin_info.get("bin", "N/A"))
                        network = bin_info.get("network", "")
                        bin_name = f"{network} {bin_number}"
                        print(f"   {Colors.CYAN}Bin {i}: {bin_name}{Colors.ENDC}")
                    else:
                        print(f"   {Colors.CYAN}Bin {i}: {bin_info}{Colors.ENDC}")
                        
                if len(bins) > 3:
                    print(f"   {Colors.CYAN}... and {len(bins) - 3} more bins{Colors.ENDC}")
    else:
        print(f"{Colors.RED}Failed to get bins: {bins_result}{Colors.ENDC}")
        
    # Duration
    duration = (datetime.now() - start_time).total_seconds()
    print(f"\n{Colors.BOLD}Test completed in {duration:.2f} seconds{Colors.ENDC}")
    print(f"\n{Colors.GREEN}✨ You're all set to use the API-Card Python SDK!{Colors.ENDC}")
    print(f"\n{Colors.BOLD}For more information, visit: {Colors.UNDERLINE}https://api-card.com/docs{Colors.ENDC}")

def run_script(script_name):
    """Run a Python script and parse its output"""
    script_path = os.path.join(EXAMPLES_DIR, script_name)
    try:
        # Run in a controlled environment to capture the result
        temp_file = f"temp_result_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.txt"
        cmd = f"{sys.executable} {script_path} > {temp_file}"
        os.system(cmd)
        
        # Read the output from temp file
        if os.path.exists(temp_file):
            with open(temp_file, 'r', encoding='utf-8', errors='ignore') as f:
                output = f.read().strip()
            # Clean up
            try:
                os.remove(temp_file)
            except:
                pass  # Ignore cleanup errors
        else:
            return {'Good': False, 'Message': f"Script produced no output"}
            
        # For auth.py, check for successful response
        if script_name == "auth.py" and "Authentication successful" in output:
            return {'Good': True, 'Status': 0}
            
        # Extract the JSON from the output
        # Format is typically "Balance: {'Status': 0, 'Good': True, ...}"
        if ':' in output:
            try:
                output = output.split(':', 1)[1].strip()
            except:
                pass  # Keep original if splitting fails
        
        try:
            # Try to parse as JSON/Python dict
            result = eval(output)
            return result
        except:
            # For successful output that can't be parsed as JSON
            if "successful" in output.lower():
                return {'Good': True, 'Status': 0, 'Result': output}
            # Return as string if not parseable
            return {'Good': False, 'Message': f"Could not parse output: {output}"}
    except Exception as e:
        return {'Good': False, 'Message': f"Error running script: {e}"}

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Test run interrupted by user.{Colors.ENDC}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}An unexpected error occurred: {str(e)}{Colors.ENDC}")
        sys.exit(1)
