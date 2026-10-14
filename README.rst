Jinasena : SubModule : Purchase : Local Purchase
================================================

Bug fixes for the Local Purchase (Credit) workflow

BugFix-Purchase already moves the "Update PR" step into Confirm and hides
the manual Update PR button, but the Studio view on the purchase order
form still only showed Confirm when ``x_studio_pr_update`` was set and
``x_studio_receive_status`` was 'Pending', so Confirm never appeared.
This module's view inheritance removes those two outdated conditions.

Information
-----------

* Technical name: ``Jinasena_Local_Purchase``
* Version: ``17.0.1.0.4``
* Depends on: ``base_setup``, ``purchase``, ``BugFix-Purchase``
* Author: Jinasena Agricultural Machinery (Pvt) Ltd.
* License: LGPL-3

Further documentation
---------------------

* Functional documentation: ``Functional_Documentation.md``
* Change history: ``CHANGELOG.md``
