Jinasena : SubModule : Purchase : Local Purchase
================================================

Bug fixes for the Local Purchase (Credit) workflow

BugFix-Purchase already moves the "Update PR" step into Confirm and hides
the manual Update PR button, but the Studio view on the purchase order
form still only showed Confirm when ``pr_update`` was set and
``receive_status`` was 'Pending', so Confirm never appeared.
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

.. BEGIN rename-studio-names

Naming and upgrade notes
========================

This module was first built in Odoo Studio and later moved to code. On 2026-11-11 (branches ``Rename-HelpdeskRepair`` for the Repair names, then ``Rename-All``) the Studio names were replaced: the Studio prefix ``x_studio_`` / ``x_`` was removed and the rest of each name kept (``x_studio_pr_number`` -> ``pr_number``). Where that name already exists on the model (a field or method of Odoo or of our code, including mixins such as mail.thread), or is a Python keyword or a PostgreSQL reserved word, the repo name is the prefix instead (``x_studio_locked`` on sale.order -> ``sales_locked``). ``x_active`` became ``active``. Custom models follow the same rule (``x_purchase_request_mt`` -> ``purchase_request_mt``). Studio-numbered XML ids (``server_action_1234_...``, ``view_5678_odoo_studio_...``) got clean names. New custom fields and models follow the same rule: a plain name, and the repo name as prefix only when the plain name is taken.

Kept with ``x_`` on purpose: test models and their fields, fields that exist only in the database (not declared in code), ``x_planNN_id`` (created by Odoo analytic plans) and many2many table and column names (they hold the data; fields between renamed models name their tables explicitly).

Upgrading: the database is renamed by pre-migration scripts before the module loads, so records keep their ids. Version ``17.0.1.0.6`` runs, in order: the Repair rename of branch ``Rename-HelpdeskRepair`` (``pre-01`` .. ``pre-03``, skipped where it already ran), then the fields (``pre-10-fields``), the custom models (``pre-20-models``) and the XML ids (``pre-30-xmlids``). The same scripts ship in every module of the set; upgrading any one of them renames everything once. Log lines start with ``Studio field rename:``, ``Studio xmlid rename:`` and ``Studio model rename:``. If a new name already exists in the database the upgrade stops and rolls back (``RenameConflictError``). The full old -> new lists are the CSV files next to each script.

.. END rename-studio-names
